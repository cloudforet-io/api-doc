---
description:  
---
# Helloworld

>  **Package : spaceone.api.sample.v1**

## HelloWorld

{% hint style="info" %}
**HelloWorld Methods:**
desc: The greeting service definition.
{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**say_hello**](helloworld.md#say_hello)|   [HelloRequest](helloworld.md#hellorequest) |   [HelloReply](helloworld.md#helloreply) | Sends a greeting |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**say_hello**](helloworld.md#say_hello) </div> | <div style="width:200px; text-align:center;">    [HelloRequest](helloworld.md#hellorequest)  </div> | <div style="width:200px; text-align:center;">   [HelloReply](helloworld.md#helloreply)  </div> | <div style="width:400px;"> Sends a greeting </div> | 
 

 
### say_hello

> Sends a greeting

| Type | Message |
| :--- | :--- |
| Request | [HelloRequest](helloworld.md#hellorequest) |
| Response |  [HelloReply](helloworld.md#helloreply)  |


## 

## Message

### HelloReply
| Field | Type |  Description |
| :--- | :--- | :--- |
| message |string | |

### HelloRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
