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


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**say_hello**](helloworld.md#say_hello)|   [HelloRequest](helloworld.md#hellorequest) |   [HelloReply](helloworld.md#helloreply) | 
 

 
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
