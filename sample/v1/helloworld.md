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


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**say_hello**](helloworld.md#say_hello)|   [HelloRequest](helloworld.md#hellorequest) |   [HelloReply](helloworld.md#helloreply) | Sends a greeting | 
 

 
### say_hello

> Sends a greeting

| Type | Message |
| :--- | :--- |
| Request | [HelloRequest](helloworld.md#hellorequest) |
| Response |  [HelloReply](helloworld.md#helloreply)  |


## 

## Message

### HelloReply
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | message |string | |

### HelloRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
