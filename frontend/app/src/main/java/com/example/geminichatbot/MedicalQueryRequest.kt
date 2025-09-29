package com.example.geminichatbot

import com.google.gson.annotations.SerializedName

data class MedicalQueryRequest(
    val query: String,
    @SerializedName("conversation_history")
    val conversation_history: List<MessageModel>,
    @SerializedName("session_id")
    val sessionId: String
)
