---
description:  
---
# Auth

>  **Package : spaceone.api.identity.plugin**

## Auth

{% hint style="info" %}
**Auth Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**init**](auth.md#init)|   [InitRequest](auth.md#initrequest) |   [PluginInfo](auth.md#plugininfo) |
| [**verify**](auth.md#verify)|   [VerifyRequest](auth.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**find**](auth.md#find)|   [FindRequest](auth.md#findrequest) |   [UsersInfo](auth.md#usersinfo) |
| [**login**](auth.md#login)|   [LoginRequest](auth.md#loginrequest) |   [UserInfo](auth.md#userinfo) | 
 

 
### init


| Type | Message |
| :--- | :--- |
| Request | [InitRequest](auth.md#initrequest) |
| Response |  [PluginInfo](auth.md#plugininfo)  |
 
 

 
### verify


| Type | Message |
| :--- | :--- |
| Request | [VerifyRequest](auth.md#verifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### find


| Type | Message |
| :--- | :--- |
| Request | [FindRequest](auth.md#findrequest) |
| Response |  [UsersInfo](auth.md#usersinfo)  |
 
 

 
### login


| Type | Message |
| :--- | :--- |
| Request | [LoginRequest](auth.md#loginrequest) |
| Response |  [UserInfo](auth.md#userinfo)  |


## 

## Message

### AuthVerifyInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### FindRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| user_id |string|❌| |
| keyword |string|❌| |
| schema |string|❌| |

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### LoginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| user_credentials |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### UserInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">email</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">mobile</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">group</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>UNIDENTIFIED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UsersInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of UserInfo](auth.md#userinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| more |bool | |

### VerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |
