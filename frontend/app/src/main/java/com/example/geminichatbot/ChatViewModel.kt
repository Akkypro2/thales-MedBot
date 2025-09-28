import android.app.Application
import android.content.Context
import android.net.ConnectivityManager
import android.net.NetworkCapabilities
import android.os.Build
import android.util.Log
import androidx.annotation.RequiresApi
import androidx.compose.runtime.mutableStateListOf
import com.example.geminichatbot.RetrofitClient
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.geminichatbot.Constants
import com.example.geminichatbot.MedicalChatApi
import com.example.geminichatbot.MedicalQueryRequest
import com.example.geminichatbot.MedicalQueryResponse
import com.example.geminichatbot.MessageModel
import com.example.geminichatbot.ui.theme.MessageRow
import kotlinx.coroutines.launch
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.withContext
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class ChatViewModel(application: Application) : AndroidViewModel(application) {

    private val _messageList = mutableStateListOf<MessageModel>()
    val messageList: List<MessageModel> = _messageList

    private val _isTyping = MutableLiveData(false)
    val isTyping: LiveData<Boolean> = _isTyping

    private val apiService = RetrofitClient.instance




    private fun isNetworkAvailable(): Boolean {
        val cm = getApplication<Application>().getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        val network = cm.activeNetwork ?: return false
        val capabilities = cm.getNetworkCapabilities(network) ?: return false
        return capabilities.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
    }


    @RequiresApi(Build.VERSION_CODES.VANILLA_ICE_CREAM)
    fun sendMessage(question: String, context: Context) {
        viewModelScope.launch {
            try {
                // Add user message
                _messageList.add(MessageModel(message = question, role = "user"))

                // Check internet connection
                if (!isNetworkAvailable()) {
                    _messageList.add(MessageModel(
                        message = "No internet connection. Please check your network.",
                        role = "model"
                    ))
                    return@launch
                }

                // Add empty bot message that will be animated
                val botMessageIndex = messageList.size
                _messageList.add(MessageModel(message = "Thinking...", role = "model"))

                // Get full response from Gemini
                val response = withContext(Dispatchers.IO) {
                    apiService.sendMedicalQuery(
                        MedicalQueryRequest(
                            query = question,
                            conversation_history = messageList.filter{it.role != "model" || it.message != "Thinking..."}
                        )
                    )
                }

                val formattedResponse = formatMedicalResponse(response)
                // Animate the response word by word
                animateTextResponse(formattedResponse, botMessageIndex)

            } catch (e: Exception) {
                _messageList.add(MessageModel(
                    message = "Something went wrong. Please try again.",
                    role = "model"
                ))
            }
        }
    }

    private fun formatMedicalResponse(response: MedicalQueryResponse): String{
        var formattedText = response.response

        if(!response.sources.isNullOrEmpty()){
            formattedText += "\n\n sources\n"
            response.sources.forEach { source->
                formattedText += "- $source\n"
            }
        }
        return formattedText
    }
    private suspend fun animateTextResponse(fullText: String, messageIndex: Int) {
        val words = fullText.split(" ")
        var currentText = ""

        _isTyping.value = true

        for (word in words) {
            currentText += if (currentText.isEmpty()) word else " $word"

            // Update the message at the specific index
            _messageList[messageIndex] = _messageList[messageIndex].copy(message = currentText)

            // Delay between words (adjust speed here)
            delay(50) // 100ms between each word
        }

        _isTyping.value = false
    }

}