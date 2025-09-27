package com.example.geminichatbot

import retrofit2.http.Body
import retrofit2.http.POST

interface MedicalChatApi {
    @POST("ask")
    suspend fun sendMedicalQuery(@Body request: MedicalQueryRequest): MedicalQueryResponse
}