---
title: "Post"
linkTitle: "Post"
weight: 3
bookFlatSection: true
---
# [Post](#Post)
A Post is a message published on a Board. It also provides notifications to Projects affected by the Post.


>  **Package : spaceone.api.board.v1**

<br>
<br>

## Post





**Post Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Post#create) | [CreatePostRequest](Post#createpostrequest) | [PostInfo](Post#postinfo) |
| [**update**](./Post#update) | [UpdatePostRequest](Post#updatepostrequest) | [PostInfo](Post#postinfo) |
| [**send_notification**](./Post#send_notification) | [SendNotificationRequest](Post#sendnotificationrequest) | [Empty](Post#empty) |
| [**delete**](./Post#delete) | [PostRequest](Post#postrequest) | [Empty](Post#empty) |
| [**get**](./Post#get) | [GetPostRequest](Post#getpostrequest) | [PostInfo](Post#postinfo) |
| [**list**](./Post#list) | [PostQuery](Post#postquery) | [PostsInfo](Post#postsinfo) |
| [**stat**](./Post#stat) | [PostStatQuery](Post#poststatquery) | [Struct](Post#struct) |



    
<br>

### create

Creates a new Post under a specific Board. You must specify the `board_id`, `title`, and `contents`. The parameter `category` is not required but can be set in the scope of `categories` specified in the parent Board. You can make the new Post pinned or pop up by adjusting the parameters.



> **POST** /board/v1/post/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreatePostRequest](./Post#createpostrequest)

* **board_id** (string)   `Required` 


* **title** (string)   `Required` 


* **contents** (string)   `Required` 


* **category** (string)  


* **options** (Struct)  


* **writer** (string)  


* **files** (string)  `Repeated`   


* **domain_id** (string)  





{{< highlight json >}}
{
   "board_id": "board-123456789012",
   "category": "developer",
   "title": "title",
   "contents": "This is contents.",
   "options": {"is_popup": true},
   "writer": "user1",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PostInfo](#POSTINFO)
* **board_id** (string)   `Required` 

* **post_id** (string)   `Required` 

* **post_type** (PostType)   `Required` 

* **category** (string)   `Required` 

* **title** (string)   `Required` 

* **contents** (string)   `Required` 

* **options** (Struct)   `Required` 

* **view_count** (int32)   `Required` 

* **writer** (string)   `Required` 

* **scope** (Scope)   `Required` 

* **files** (ListValue)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **user_domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
         "board_id": "board-123456789012",
         "post_id": "post-123456789012",
         "post_type": "INTERNAL",
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Post. You can make changes in Post settings, except `board_id`, `post_id`, and `domain_id`.



> **POST** /board/v1/post/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdatePostRequest](./Post#updatepostrequest)

* **board_id** (string)   `Required` 


* **post_id** (string)   `Required` 


* **category** (string)  


* **title** (string)  


* **contents** (string)  


* **options** (Struct)  


* **writer** (string)  


* **files** (string)  `Repeated`   


* **domain_id** (string)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PostInfo](#POSTINFO)
* **board_id** (string)   `Required` 

* **post_id** (string)   `Required` 

* **post_type** (PostType)   `Required` 

* **category** (string)   `Required` 

* **title** (string)   `Required` 

* **contents** (string)   `Required` 

* **options** (Struct)   `Required` 

* **view_count** (int32)   `Required` 

* **writer** (string)   `Required` 

* **scope** (Scope)   `Required` 

* **files** (ListValue)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **user_domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
         "board_id": "board-123456789012",
         "post_id": "post-123456789012",
         "post_type": "INTERNAL",
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### send_notification

Not Implemented



> **POST** /board/v1/post/send-notification
>






    
<br>

### delete

Deletes a specific Post. You must specify the `post_id` of the Post to delete, and the `board_id` of the Board where the child Post to delete belongs.



> **POST** /board/v1/post/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[PostRequest](./Post#postrequest)

* **board_id** (string)   `Required` 


* **post_id** (string)   `Required` 


* **domain_id** (string)  





{{< highlight json >}}
{
   "board_id": "board-b9aa34e65c60",
   "post_id": "post-2118473ce15e",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.



> **POST** /board/v1/post/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetPostRequest](./Post#getpostrequest)

* **board_id** (string)   `Required` 


* **post_id** (string)   `Required` 


* **only** (string)  `Repeated`   


* **domain_id** (string)  





{{< highlight json >}}
{
   "board_id": "board-b9aa34e65c60",
   "post_id": "post-2118473ce15e",
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PostInfo](#POSTINFO)
* **board_id** (string)   `Required` 

* **post_id** (string)   `Required` 

* **post_type** (PostType)   `Required` 

* **category** (string)   `Required` 

* **title** (string)   `Required` 

* **contents** (string)   `Required` 

* **options** (Struct)   `Required` 

* **view_count** (int32)   `Required` 

* **writer** (string)   `Required` 

* **scope** (Scope)   `Required` 

* **files** (ListValue)   `Required` 

* **domain_id** (string)   `Required` 

* **user_id** (string)   `Required` 

* **user_domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
         "board_id": "board-123456789012",
         "post_id": "post-123456789012",
         "post_type": "INTERNAL",
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Posts. You can use a query to get a filtered list of Posts.



> **POST** /board/v1/post/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[PostQuery](./Post#postquery)

* **board_id** (string)   `Required` 


* **post_id** (string)  


* **post_type** (PostType)  


* **category** (string)  


* **writer** (string)  


* **scope** (Scope)  


* **user_id** (string)  


* **user_domain_id** (string)  


* **domain_id** (string)  


* **query** (Query)  





{{< highlight json >}}
{
   "board_id": "board-b9aa34e65c60",
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PostsInfo](#POSTSINFO)
* **results** (PostInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
     "results": [
         {
             "board_id": "board-b9aa34e65c60",
             "post_id": "post-2118473ce15e",
             "post_type": "INTERNAL",
             "category": "spaceone",
             "title": "title2",
             "contents": "this is contents2.",
             "options": {
                 "is_popup": false,
                 "is_pinned": true
             },
             "view_count": 3,
             "writer": "seolmin2",
             "scope": "DOMAIN",
             "domain_id": "domain-58010aa2e451",
             "user_id": "user1@email.com",
             "created_at": "2022-06-13T01:06:23.732Z",
             "updated_at": "2022-06-13T01:06:23.732Z"
         },
         {
             "board_id": "board-b9aa34e65c60",
             "post_id": "post-532ae1191233",
             "post_type": "INTERNAL",
             "category": "flower",
             "title": "작업공지",
             "contents": "This is description",
             "options": {
                 "is_pinned": true,
                 "is_popup": true
             },
             "writer": "권설민",
             "scope": "PUBLIC",
             "user_id": "supervisor",
             "created_at": "2022-06-10T07:01:44.384Z",
             "updated_at": "2022-06-10T07:01:44.384Z"
         }
     ],
     "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /board/v1/post/stat
>






    


<br>
<br>

## Message



### CreatePostRequest
* **board_id** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **contents** (string)   `Required` 

    
* **category** (string)  

    
* **options** (Struct)  

    
* **writer** (string)  

    
* **files** (string)  `Repeated`   

    
* **domain_id** (string)  

    <br>

### GetPostRequest
* **board_id** (string)   `Required` 

    
* **post_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    
* **domain_id** (string)  

    <br>

### PostInfo
* **board_id** (string)   `Required` 

    
* **post_id** (string)   `Required` 

    
* **post_type** (PostType)   `Required` 

    
* **category** (string)   `Required` 

    
* **title** (string)   `Required` 

    
* **contents** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **view_count** (int32)   `Required` 

    
* **writer** (string)   `Required` 

    
* **scope** (Scope)   `Required` 

    
* **files** (ListValue)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **user_domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PostQuery
* **board_id** (string)   `Required` 

    
* **post_id** (string)  

    
* **post_type** (PostType)  

    
* **category** (string)  

    
* **writer** (string)  

    
* **scope** (Scope)  

    
* **user_id** (string)  

    
* **user_domain_id** (string)  

    
* **domain_id** (string)  

    
* **query** (Query)  

    <br>

### PostRequest
* **board_id** (string)   `Required` 

    
* **post_id** (string)   `Required` 

    
* **domain_id** (string)  

    <br>

### PostStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### PostsInfo
* **results** (PostInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### SendNotificationRequest
* **board_id** (string)   `Required` 

    
* **post_id** (string)   `Required` 

    
* **domain_id** (string)  

    <br>

### UpdatePostRequest
* **board_id** (string)   `Required` 

    
* **post_id** (string)   `Required` 

    
* **category** (string)  

    
* **title** (string)  

    
* **contents** (string)  

    
* **options** (Struct)  

    
* **writer** (string)  

    
* **files** (string)  `Repeated`   

    
* **domain_id** (string)  

    <br>
