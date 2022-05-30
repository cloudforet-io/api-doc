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


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**say_hello**](helloworld.md#say_hello)|   [HelloRequest](helloworld.md#hellorequest) |   [HelloReply](helloworld.md#helloreply) | Sends a greeting |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">say_hello</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   HelloRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   HelloReply </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Sends a greeting</td>
    </tr></tbody>
</table> 
 

 
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
