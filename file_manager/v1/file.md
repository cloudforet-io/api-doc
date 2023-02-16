---
description:  
---
# File

>  **Package : spaceone.api.file_manager.v1**

## File

{% hint style="info" %}
**File Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](file.md#add)|   [CreateFileRequest](file.md#createfilerequest) |   [FileInfo](file.md#fileinfo) |
| [**update**](file.md#update)|   [UpdateFileRequest](file.md#updatefilerequest) |   [FileInfo](file.md#fileinfo) |
| [**delete**](file.md#delete)|   [FileRequest](file.md#filerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get_download_url**](file.md#get_download_url)|   [FileRequest](file.md#filerequest) |   [FileInfo](file.md#fileinfo) |
| [**get**](file.md#get)|   [GetFileRequest](file.md#getfilerequest) |   [FileInfo](file.md#fileinfo) |
| [**list**](file.md#list)|   [FileQuery](file.md#filequery) |   [FilesInfo](file.md#filesinfo) |
| [**stat**](file.md#stat)|   [FileStatQuery](file.md#filestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### add
> **POST** /file-manager/v1/file/add
>


| Type | Message |
| :--- | :--- |
| Request | [CreateFileRequest](file.md#createfilerequest) |
| Response |  [FileInfo](file.md#fileinfo)  |
 
 

 
### update
> **POST** /file-manager/v1/file/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateFileRequest](file.md#updatefilerequest) |
| Response |  [FileInfo](file.md#fileinfo)  |
 
 

 
### delete
> **POST** /file-manager/v1/file/delete
>


| Type | Message |
| :--- | :--- |
| Request | [FileRequest](file.md#filerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get_download_url
> **POST** /file-manager/v1/file/get-download-url
>


| Type | Message |
| :--- | :--- |
| Request | [FileRequest](file.md#filerequest) |
| Response |  [FileInfo](file.md#fileinfo)  |
 
 

 
### get
> **POST** /file-manager/v1/file/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetFileRequest](file.md#getfilerequest) |
| Response |  [FileInfo](file.md#fileinfo)  |
 
 

 
### list
> **POST** /file-manager/v1/file/list
>


| Type | Message |
| :--- | :--- |
| Request | [FileQuery](file.md#filequery) |
| Response |  [FilesInfo](file.md#filesinfo)  |
 
 

 
### stat
> **POST** /file-manager/v1/file/stat
>


| Type | Message |
| :--- | :--- |
| Request | [FileStatQuery](file.md#filestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateFileRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| reference |[FileReference](file.md#filereference)|✘| |
| domain_id |string|✘| |

### FileInfo
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
      <td style="text-align:left; width:100px;">file_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>STATE_NONE</li>
          	<li>PENDING</li>
          	<li>DONE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>PUBLIC</li>
          	<li>DOMAIN</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">file_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upload_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upload_options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">download_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reference</td>
      <td style="text-align:left"><a href="file.md#filereference">FileReference</a></td>
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
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### FileQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">file_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>STATE_NONE</li>
          	<li>PENDING</li>
          	<li>DONE</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>PUBLIC</li>
          	<li>DOMAIN</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">file_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">user_domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### FileReference
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| resource_id |string | |

### FileRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| file_id |string|✔| |
| domain_id |string|✘| |

### FileStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### FilesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of FileInfo](file.md#fileinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetFileRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| file_id |string|✔| |
| domain_id |string|✘| |
| only |list of string|✘| |

### UpdateFileRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| file_id |string|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| reference |[FileReference](file.md#filereference)|✘| |
| domain_id |string|✘| |
