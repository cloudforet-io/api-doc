---
title: "Post"
linkTitle: "Post"
weight: 3
bookFlatSection: true
---
# [Post](#Post)
desc: A Post is a message published on a Board. It also provides notifications to Projects affected by the Post.


>  **Package : spaceone.api.board.v1**

<br>
<br>

## Post


**Post Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Post#create) | [CreatePostRequest](Post#createpostrequest) | [PostInfo](./Post#postinfo) |
| [**update**](./Post#update) | [UpdatePostRequest](Post#updatepostrequest) | [PostInfo](./Post#postinfo) |
| [**send_notification**](./Post#send_notification) | [SendNotificationRequest](Post#sendnotificationrequest) | [Empty](./Post#empty) |
| [**delete**](./Post#delete) | [PostRequest](Post#postrequest) | [Empty](./Post#empty) |
| [**get**](./Post#get) | [GetPostRequest](Post#getpostrequest) | [PostInfo](./Post#postinfo) |
| [**list**](./Post#list) | [PostQuery](Post#postquery) | [PostsInfo](./Post#postsinfo) |
| [**stat**](./Post#stat) | [PostStatQuery](Post#poststatquery) | [Struct](./Post#struct) |



    
<br>

### create

> **POST** /board/v1/board/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /board/v1/board/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### send_notification

> **POST** /board/v1/board/send-notification
>




 {{< tabs " send_notification " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /board/v1/board/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /board/v1/board/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /board/v1/board/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /board/v1/board/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreatePostRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **category** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: true*

    
* **contents** (string)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **writer** (string)  `Required` 

  *is_required: false*

    
* **files** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### GetPostRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **post_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### PostInfo
* **board_id** (string)  `Required` 

    
* **post_id** (string)  `Required` 

    
* **post_type** (PostType)  `Required` 

    
* **category** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **contents** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **view_count** (int32)  `Required` 

    
* **writer** (string)  `Required` 

    
* **scope** (Scope)  `Required` 

    
* **files** (ListValue)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **user_domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### PostQuery
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **post_id** (string)  `Required` 

  *is_required: false*

    
* **post_type** (PostType)  `Required` 

  *is_required: false*

    
* **category** (string)  `Required` 

  *is_required: false*

    
* **writer** (string)  `Required` 

  *is_required: false*

    
* **scope** (Scope)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **user_domain_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    
* **query** (Query)  `Required` 

  *is_required: false*

    <br>

### PostRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **post_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### PostStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PostsInfo
* **results** (PostInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### SendNotificationRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **post_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### UpdatePostRequest
* **board_id** (string)  `Required` 

  *is_required: true*

    
* **post_id** (string)  `Required` 

  *is_required: true*

    
* **category** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **contents** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **writer** (string)  `Required` 

  *is_required: false*

    
* **files** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>
