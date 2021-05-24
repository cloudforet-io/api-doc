---
description:  
---
# User channel

>  **Package : spaceone.api.notification.v1**

## UserChannel

{% hint style="info" %}
**UserChannel Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](user-channel.md#create)|   [CreateUserChannelRequest](user-channel.md#createuserchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |  |
| 2 | [**update**](user-channel.md#update)|   [UpdateUserChannelRequest](user-channel.md#updateuserchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |  |
| 3 | [**set_subscription**](user-channel.md#set_subscription)|   [UpdateUserChannelSubscriptionRequest](user-channel.md#updateuserchannelsubscriptionrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |  |
| 4 | [**enable**](user-channel.md#enable)|   [UserChannelRequest](user-channel.md#userchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |  |
| 5 | [**disable**](user-channel.md#disable)|   [UserChannelRequest](user-channel.md#userchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |  |
| 6 | [**delete**](user-channel.md#delete)|   [UserChannelRequest](user-channel.md#userchannelrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**get**](user-channel.md#get)|   [GetUserChannelRequest](user-channel.md#getuserchannelrequest) |   [UserChannelInfo](user-channel.md#userchannelinfo) |  |
| 8 | [**list**](user-channel.md#list)|   [UserChannelQuery](user-channel.md#userchannelquery) |   [UserChannelsInfo](user-channel.md#userchannelsinfo) |  |
| 9 | [**stat**](user-channel.md#stat)|   [UserChannelStatQuery](user-channel.md#userchannelstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /notification/v1/user-channels
>


| Type | Message |
| :--- | :--- |
| Request | [CreateUserChannelRequest](user-channel.md#createuserchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### update
> **PUT** /notification/v1/user-channel/{user_channel_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateUserChannelRequest](user-channel.md#updateuserchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### set_subscription
> **PUT** /notification/v1/user-channel/{user_channel_id}/subscription
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateUserChannelSubscriptionRequest](user-channel.md#updateuserchannelsubscriptionrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/user-channel/{user_channel_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [UserChannelRequest](user-channel.md#userchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### disable
> **PUT** /notification/v1/user-channel/{user_channel_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [UserChannelRequest](user-channel.md#userchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/user-channel/{user_channel_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UserChannelRequest](user-channel.md#userchannelrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/user-channel/{user_channel_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetUserChannelRequest](user-channel.md#getuserchannelrequest) |
| Response |  [UserChannelInfo](user-channel.md#userchannelinfo)  |
 
 

 
### list
> **GET** /notification/v1/user-channels
>
> **POST** /notification/v1/user-channels/search



| Type | Message |
| :--- | :--- |
| Request | [UserChannelQuery](user-channel.md#userchannelquery) |
| Response |  [UserChannelsInfo](user-channel.md#userchannelsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/user-channels/stat
>


| Type | Message |
| :--- | :--- |
| Request | [UserChannelStatQuery](user-channel.md#userchannelstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateUserChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | protocol_id |string|✅| |
| 2 | name |string|✅| |
| 3 | schema |string|✅| |
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 5 | is_subscribe |bool|❌| |
| 6 | subscriptions |list of string|❌| |
| 7 | schedule |[UserChannelSchedule](user-channel.md#userchannelschedule)|❌| |
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 9 | user_id |string|✅| |
| 10 | domain_id |string|✅| |

### GetUserChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_channel_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateUserChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_channel_id |string|✅| |
| 2 | name |string|❌| |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | schedule |[UserChannelSchedule](user-channel.md#userchannelschedule)|❌| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | domain_id |string|✅| |

### UpdateUserChannelSubscriptionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_channel_id |string|✅| |
| 2 | is_subscribe |bool|✅| |
| 3 | subscriptions |list of string|❌| |
| 4 | domain_id |string|✅| |

### UserChannelInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">user_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">is_subscribe</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">subscriptions</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">schedule</td>
      <td style="text-align:left"><a href="user-channel.md#userchannelschedule">UserChannelSchedule</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UserChannelQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">user_channel_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UserChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | user_channel_id |string|✅| |
| 2 | domain_id |string|✅| |

### UserChannelSchedule
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">day_of_week</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MON</li>
          	<li>TUE</li>
          	<li>WED</li>
          	<li>THU</li>
          	<li>FRI</li>
          	<li>SAT</li>
          	<li>SUN</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">start_hour</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">end_hour</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### UserChannelStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### UserChannelsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of UserChannelInfo](user-channel.md#userchannelinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
