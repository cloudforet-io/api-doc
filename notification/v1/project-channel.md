---
description:  
---
# Project channel

>  **Package : spaceone.api.notification.v1**

## ProjectChannel

{% hint style="info" %}
**ProjectChannel Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](project-channel.md#create)|   [CreateProjectChannelRequest](project-channel.md#createprojectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |  |
| 2 | [**update**](project-channel.md#update)|   [UpdateProjectChannelRequest](project-channel.md#updateprojectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |  |
| 3 | [**set_subscription**](project-channel.md#set_subscription)|   [UpdateSubscriptionRequest](project-channel.md#updatesubscriptionrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |  |
| 4 | [**enable**](project-channel.md#enable)|   [ProjectChannelRequest](project-channel.md#projectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |  |
| 5 | [**disable**](project-channel.md#disable)|   [ProjectChannelRequest](project-channel.md#projectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |  |
| 6 | [**delete**](project-channel.md#delete)|   [ProjectChannelRequest](project-channel.md#projectchannelrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**get**](project-channel.md#get)|   [GetProjectChannelRequest](project-channel.md#getprojectchannelrequest) |   [ProjectChannelInfo](project-channel.md#projectchannelinfo) |  |
| 8 | [**list**](project-channel.md#list)|   [ProjectChannelQuery](project-channel.md#projectchannelquery) |   [ProjectChannelsInfo](project-channel.md#projectchannelsinfo) |  |
| 9 | [**stat**](project-channel.md#stat)|   [ProjectChannelStatQuery](project-channel.md#projectchannelstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /notification/v1/project-channels
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProjectChannelRequest](project-channel.md#createprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### update
> **PUT** /notification/v1/project-channel/{project_channel_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectChannelRequest](project-channel.md#updateprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### set_subscription
> **PUT** /notification/v1/project-channel/{project_channel_id}/subscription
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateSubscriptionRequest](project-channel.md#updatesubscriptionrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/project-channel/{project_channel_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### disable
> **PUT** /notification/v1/project-channel/{project_channel_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/project-channel/{project_channel_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelRequest](project-channel.md#projectchannelrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/project-channel/{project_channel_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetProjectChannelRequest](project-channel.md#getprojectchannelrequest) |
| Response |  [ProjectChannelInfo](project-channel.md#projectchannelinfo)  |
 
 

 
### list
> **GET** /notification/v1/project-channels
>
> **POST** /notification/v1/project-channels/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelQuery](project-channel.md#projectchannelquery) |
| Response |  [ProjectChannelsInfo](project-channel.md#projectchannelsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/project-channels/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectChannelStatQuery](project-channel.md#projectchannelstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProjectChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | protocol_id |string|✅| |
| 2 | name |string|✅| |
| 3 | schema |string|✅| |
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 5 | subscriptions |list of string|❌| |
| 6 | notification_level |string|❌| |
| 7 | schedule |[ProjectChannelSchedule](project-channel.md#projectchannelschedule)|❌| |
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 9 | project_id |string|✅| |
| 10 | domain_id |string|✅| |

### GetProjectChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_channel_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### ProjectChannelInfo
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
      <td style="text-align:left">project_channel_id</td>
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
      <td style="text-align:left">subscriptions</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">notification_level</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">schedule</td>
      <td style="text-align:left"><a href="project-channel.md#projectchannelschedule">ProjectChannelSchedule</a></td>
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
      <td style="text-align:left">project_id</td>
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



### ProjectChannelQuery
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
      <td style="text-align:left">project_channel_id</td>
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
      <td style="text-align:left">notification_level</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ProjectChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_channel_id |string|✅| |
| 2 | domain_id |string|✅| |

### ProjectChannelSchedule
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



### ProjectChannelStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ProjectChannelsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ProjectChannelInfo](project-channel.md#projectchannelinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProjectChannelRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_channel_id |string|✅| |
| 2 | name |string|❌| |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | subscriptions |list of string|❌| |
| 5 | notification_level |string|❌| |
| 6 | schedule |[ProjectChannelSchedule](project-channel.md#projectchannelschedule)|❌| |
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 8 | domain_id |string|✅| |

### UpdateSubscriptionRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_channel_id |string|✅| |
| 2 | is_subscribe |bool|✅| |
| 3 | subscriptions |list of string|❌| |
| 4 | domain_id |string|✅| |
