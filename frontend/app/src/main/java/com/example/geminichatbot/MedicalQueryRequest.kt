package com.example.geminichatbot

data class MedicalQueryRequest(
    val query: String,
    val conversation_history: List<MessageModel>
)
