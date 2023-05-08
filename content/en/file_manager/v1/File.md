---
title: "File"
linkTitle: "File"
weight: 3
bookFlatSection: true
---
# [File](#File)



>  **Package : spaceone.api.file_manager.v1**

<br>
<br>

## File


**File Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./File#add) | [CreateFileRequest](File#createfilerequest) | [FileInfo](./File#fileinfo) |
| [**update**](./File#update) | [UpdateFileRequest](File#updatefilerequest) | [FileInfo](./File#fileinfo) |
| [**delete**](./File#delete) | [FileRequest](File#filerequest) | [Empty](./File#empty) |
| [**get_download_url**](./File#get_download_url) | [FileRequest](File#filerequest) | [FileInfo](./File#fileinfo) |
| [**get**](./File#get) | [GetFileRequest](File#getfilerequest) | [FileInfo](./File#fileinfo) |
| [**list**](./File#list) | [FileQuery](File#filequery) | [FilesInfo](./File#filesinfo) |
| [**stat**](./File#stat) | [FileStatQuery](File#filestatquery) | [Struct](./File#struct) |



    
<br>

### add

> **POST** /file-manager/v1/file/add
>




 {{< tabs " add " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /file-manager/v1/file/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /file-manager/v1/file/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get_download_url

> **POST** /file-manager/v1/file/get-download-url
>




 {{< tabs " get_download_url " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /file-manager/v1/file/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /file-manager/v1/file/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /file-manager/v1/file/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateFileRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **reference** (FileReference)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### FileInfo
* **file_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (FileState)  `Required` 

    
* **scope** (FileScope)  `Required` 

    
* **file_type** (string)  `Required` 

    
* **upload_url** (string)  `Required` 

    
* **upload_options** (Struct)  `Required` 

    
* **download_url** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **reference** (FileReference)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **user_domain_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### FileQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **file_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (FileState)  `Required` 

  *is_required: false*

    
* **scope** (FileScope)  `Required` 

  *is_required: false*

    
* **file_type** (string)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **resource_id** (string)  `Required` 

  *is_required: false*

    
* **user_domain_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### FileReference
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    <br>

### FileRequest
* **file_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>

### FileStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### FilesInfo
* **results** (FileInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetFileRequest
* **file_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateFileRequest
* **file_id** (string)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **reference** (FileReference)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: false*

    <br>
