---
description:  
---
# Post

>  **Package : spaceone.api.board.v1**

## Post

{% hint style="info" %}
**Post Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](post.md#create)|   [CreatePostRequest](post.md#createpostrequest) |   [PostInfo](post.md#postinfo) |  |
| [**update**](post.md#update)|   [UpdatePostRequest](post.md#updatepostrequest) |   [PostInfo](post.md#postinfo) |  |
| [**send_notification**](post.md#send_notification)|   [SendNotificationRequest](post.md#sendnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**delete**](post.md#delete)|   [PostRequest](post.md#postrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](post.md#get)|   [GetPostRequest](post.md#getpostrequest) |   [PostInfo](post.md#postinfo) |  |
| [**list**](post.md#list)|   [PostQuery](post.md#postquery) |   [PostsInfo](post.md#postsinfo) |  |
| [**stat**](post.md#stat)|   [PostStatQuery](post.md#poststatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| category |string|❌| |
| title |string|✅| |
| contents |string|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| writer |string|❌| |
| domain_id |string|❌| |

### GetPostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| post_id |string|✅| |
| only |list of string|❌| |
| domain_id |string|❌| |

### PostInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">board_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">post_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">category</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">contents</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">view_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">writer</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PostQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| post_id |string|❌| |
| category |string|❌| |
| writer |string|❌| |
| user_id |string|❌| |
| domain_id |string|❌| |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |

### PostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| post_id |string|✅| |
| domain_id |string|❌| |

### PostStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### PostsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PostInfo](post.md#postinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SendNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| post_id |string|✅| |
| domain_id |string|❌| |

### UpdatePostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✅| |
| post_id |string|✅| |
| category |string|❌| |
| title |string|❌| |
| contents |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| writer |string|❌| |
| domain_id |string|❌| |
