---
description: A Post is a message published on a Board. It also provides notifications to Projects affected by the Post.
---
# Post

>  **Package : spaceone.api.board.v1**

## Post

{% hint style="info" %}
**Post Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](post.md#create)|   [CreatePostRequest](post.md#createpostrequest) |   [PostInfo](post.md#postinfo) |
| [**update**](post.md#update)|   [UpdatePostRequest](post.md#updatepostrequest) |   [PostInfo](post.md#postinfo) |
| [**send_notification**](post.md#send_notification)|   [SendNotificationRequest](post.md#sendnotificationrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**delete**](post.md#delete)|   [PostRequest](post.md#postrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](post.md#get)|   [GetPostRequest](post.md#getpostrequest) |   [PostInfo](post.md#postinfo) |
| [**list**](post.md#list)|   [PostQuery](post.md#postquery) |   [PostsInfo](post.md#postsinfo) |
| [**stat**](post.md#stat)|   [PostStatQuery](post.md#poststatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /board/v1/board/{board_id}/posts
>

> Creates a new Post under a specific Board. You must specify the `board_id`, `title`, and `contents`. The parameter `category` is not required but can be set in the scope of `categories` specified in the parent Board. You can make the new Post pinned or pop up by adjusting the parameters.

| Type | Message |
| :--- | :--- |
| Request | [CreatePostRequest](post.md#createpostrequest) |
| Response |  [PostInfo](post.md#postinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-123456789012",
    "category": "developer",
    "title": "title",
    "contents": "This is contents.",
    "options": {
        "is_popup": true
    },
    "writer": "user1",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-123456789012",
    "post_id": "post-123456789012",
    "category": "developer",
    "title": "title",
    "contents": "This is contents.",
    "options": {
        "is_pinned": false,
        "is_popup": true
    },
    "view_count": 0,
    "writer": "user1",
    "scope": "DOMAIN",
    "domain_id": "domain-123456789012",
    "user_id": "user1@email.com",
    "created_at": "2022-01-01T01:06:23.732Z",
    "updated_at": "2022-01-01T01:06:23.732Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /board/v1/board/{board_id}/post/{post_id}
>

> Updates a specific Post. You can make changes in Post settings, except `board_id`, `post_id`, and `domain_id`.

| Type | Message |
| :--- | :--- |
| Request | [UpdatePostRequest](post.md#updatepostrequest) |
| Response |  [PostInfo](post.md#postinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-123456789012",
    "post_id": "post-2118473ce15e",
    "category": "developer",
    "title": "title2",
    "contents": "this is contents2.",
    "options": {
        "is_popup": false,
        "is_pinned": true
    },
    "writer": "user1",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-123456789012",
    "post_id": "post-123456789012",
    "category": "developer",
    "title": "title2",
    "contents": "this is contents2.",
    "options": {
        "is_popup": false,
        "is_pinned": true
    },
    "view_count": 1,
    "writer": "user1",
    "scope": "DOMAIN",
    "domain_id": "domain-123456789012",
    "user_id": "user1@email.com",
    "created_at": "2022-06-13T01:06:23.732Z",
    "updated_at": "2022-06-13T01:06:23.732Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### send_notification
> **POST** /board/v1/board/{board_id}/post/{post_id}/send-notification
>

> None

| Type | Message |
| :--- | :--- |
| Request | [SendNotificationRequest](post.md#sendnotificationrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
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

> Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.

| Type | Message |
| :--- | :--- |
| Request | [GetPostRequest](post.md#getpostrequest) |
| Response |  [PostInfo](post.md#postinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "board_id": "board-b9aa34e65c60",
    "post_id": "post-2118473ce15e",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "board_id": "board-b9aa34e65c60",
    "post_id": "post-2118473ce15e",
    "category": "flower",
    "title": "title",
    "contents": "this is contents.",
    "options": {
        "is_pinned": false,
        "is_popup": true
    },
    "view_count": 2,
    "writer": "seolmin",
    "scope": "DOMAIN",
    "domain_id": "domain-58010aa2e451",
    "user_id": "supervisor",
    "created_at": "2022-06-13T01:06:23.732Z",
    "updated_at": "2022-06-13T01:06:23.732Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
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
| board_id |string|✔| |
| category |string|✘| |
| title |string|✔| |
| contents |string|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| writer |string|✘| |
| domain_id |string|✘| |

### GetPostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| post_id |string|✔| |
| only |list of string|✘| |
| domain_id |string|✘| |

### PostInfo
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
      <td style="text-align:left; width:100px;">board_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">post_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">category</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">contents</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">view_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">writer</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">scope</td>
      <td style="text-align:left"><ul>
          	<li>SYSTEM</li>
          	<li>DOMAIN</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PostQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| post_id |string|✘| |
| category |string|✘| |
| writer |string|✘| |
| user_id |string|✘| |
| user_domain_id |string|✘| |
| domain_id |string|✘| |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |

### PostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| post_id |string|✔| |
| domain_id |string|✘| |

### PostStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### PostsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PostInfo](post.md#postinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SendNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| post_id |string|✔| |
| domain_id |string|✘| |

### UpdatePostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| board_id |string|✔| |
| post_id |string|✔| |
| category |string|✘| |
| title |string|✘| |
| contents |string|✘| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| writer |string|✘| |
| domain_id |string|✘| |
