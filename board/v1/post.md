---
description:  
---
# Post

>  **Package : spaceone.api.board.v1**

## Post

{% hint style="info" %}
**Post Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](post.md#create)|   [CreatePostRequest](post.md#createpostrequest) |   [PostInfo](post.md#postinfo) |  |
| 2 | [**update**](post.md#update)|   [UpdatePostRequest](post.md#updatepostrequest) |   [PostInfo](post.md#postinfo) |  |
| 3 | [**send_notification**](post.md#send_notification)|   [SendNotificationRequest](post.md#sendnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**delete**](post.md#delete)|   [PostRequest](post.md#postrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](post.md#get)|   [GetPostRequest](post.md#getpostrequest) |   [PostInfo](post.md#postinfo) |  |
| 6 | [**list**](post.md#list)|   [PostQuery](post.md#postquery) |   [PostsInfo](post.md#postsinfo) |  |
| 7 | [**stat**](post.md#stat)|   [PostStatQuery](post.md#poststatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /board/v1/board/{board_id}/posts
>


| Type | Message |
| :--- | :--- |
| Request | [CreatePostRequest](post.md#createpostrequest) |
| Response |  [PostInfo](post.md#postinfo)  |
 
 

 
### update
> **PUT** /board/v1/board/{board_id}/post/{post_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdatePostRequest](post.md#updatepostrequest) |
| Response |  [PostInfo](post.md#postinfo)  |
 
 

 
### send_notification
> **POST** /board/v1/board/{board_id}/post/{post_id}/send-notification
>


| Type | Message |
| :--- | :--- |
| Request | [SendNotificationRequest](post.md#sendnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### delete
> **DELETE** /board/v1/board/{board_id}/post/{post_id}
>


| Type | Message |
| :--- | :--- |
| Request | [PostRequest](post.md#postrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /board/v1/board/{board_id}/post/{post_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetPostRequest](post.md#getpostrequest) |
| Response |  [PostInfo](post.md#postinfo)  |
 
 

 
### list
> **GET** /board/v1/board/{board_id}/posts
>
> **POST** /board/v1/board/{board_id}/posts/search



| Type | Message |
| :--- | :--- |
| Request | [PostQuery](post.md#postquery) |
| Response |  [PostsInfo](post.md#postsinfo)  |
 
 

 
### stat
> **POST** /board/v1/board/{board_id}/posts/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PostStatQuery](post.md#poststatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | category |string|❌| |
| 3 | title |string|✅| |
| 4 | contents |string|✅| |
| 5 | options |[PostOptions](post.md#postoptions)|❌| |
| 6 | writer |string|❌| |
| 7 | domain_id |string|❌| |

### GetPostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | post_id |string|✅| |
| 3 | only |list of string|❌| |
| 4 | domain_id |string|❌| |

### PostInfo
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
      <td style="text-align:left">board_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">post_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">category</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">contents</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="post.md#postoptions">PostOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">view_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">writer</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PostOptions
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | is_pinned |bool | |
| 2 | is_popup |bool | |

### PostQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | post_id |string|❌| |
| 3 | category |string|❌| |
| 4 | writer |string|❌| |
| 5 | user_id |string|❌| |
| 6 | domain_id |string|❌| |
| 7 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |

### PostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | post_id |string|✅| |
| 3 | domain_id |string|❌| |

### PostStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### PostsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of PostInfo](post.md#postinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SendNotificationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | post_id |string|✅| |
| 3 | domain_id |string|❌| |

### UpdatePostRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | board_id |string|✅| |
| 2 | post_id |string|✅| |
| 3 | category |string|❌| |
| 4 | title |string|❌| |
| 5 | contents |string|❌| |
| 6 | options |[PostOptions](post.md#postoptions)|❌| |
| 7 | writer |string|❌| |
| 8 | domain_id |string|❌| |
