---
description:  
---
# Note

>  **Package : spaceone.api.monitoring.v1**

## Note

{% hint style="info" %}
**Note Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](note.md#create)|   [CreateNoteRequest](note.md#createnoterequest) |   [NoteInfo](note.md#noteinfo) |  |
| [**update**](note.md#update)|   [UpdateNoteRequest](note.md#updatenoterequest) |   [NoteInfo](note.md#noteinfo) |  |
| [**delete**](note.md#delete)|   [NoteRequest](note.md#noterequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](note.md#get)|   [GetNoteRequest](note.md#getnoterequest) |   [NoteInfo](note.md#noteinfo) |  |
| [**list**](note.md#list)|   [NoteQuery](note.md#notequery) |   [NotesInfo](note.md#notesinfo) |  |
| [**stat**](note.md#stat)|   [NoteStatQuery](note.md#notestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateNoteRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NoteInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateNoteRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NoteInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NoteRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetNoteRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NoteInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NoteQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NotesInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   NoteStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### create
> **POST** /monitoring/v1/notes
>


| Type | Message |
| :--- | :--- |
| Request | [CreateNoteRequest](note.md#createnoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/note/{note_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateNoteRequest](note.md#updatenoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/note/{note_id}
>


| Type | Message |
| :--- | :--- |
| Request | [NoteRequest](note.md#noterequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/note/{note_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetNoteRequest](note.md#getnoterequest) |
| Response |  [NoteInfo](note.md#noteinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/notes
>
> **POST** /monitoring/v1/notes/search



| Type | Message |
| :--- | :--- |
| Request | [NoteQuery](note.md#notequery) |
| Response |  [NotesInfo](note.md#notesinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/notes/stat
>


| Type | Message |
| :--- | :--- |
| Request | [NoteStatQuery](note.md#notestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateNoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✅| |
| note |string|✅| |
| domain_id |string|✅| |

### GetNoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| note_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### NoteInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| note_id |string | |
| alert_id |string | |
| note |string | |
| created_by |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |

### NoteQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| note_id |string|❌| |
| alert_id |string|❌| |
| created_by |string|❌| |
| project_id |string|❌| |
| domain_id |string|❌| |

### NoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| note_id |string|✅| |
| domain_id |string|✅| |

### NoteStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### NotesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of NoteInfo](note.md#noteinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateNoteRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| note_id |string|✅| |
| note |string|❌| |
| domain_id |string|✅| |
