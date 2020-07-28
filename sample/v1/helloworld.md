---
description:  
---
# Helloworld

>  **Package : spaceone.api.sample.v1**

## Greeter

{% hint style="info" %}
**Greeter Methods:**
desc: The greeting service definition.
{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**SayHello**](helloworld.md#SayHello)|   [HelloRequest](helloworld.md#hellorequest) |   [HelloReply](helloworld.md#helloreply) | Sends a greeting | 
 

 
### SayHello

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
| 1 | message |string| |

### HelloRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
