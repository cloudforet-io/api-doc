---
description:  
---
# Note

>  **Package : spaceone.api.monitoring.v1**

## Note

{% hint style="info" %}
**Note Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](note.md#create)|   [CreateNoteRequest](note.md#createnoterequest) |   [NoteInfo](note.md#noteinfo) |  |
| 2 | [**update**](note.md#update)|   [UpdateNoteRequest](note.md#updatenoterequest) |   [NoteInfo](note.md#noteinfo) |  |
| 3 | [**delete**](note.md#delete)|   [NoteRequest](note.md#noterequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](note.md#get)|   [GetNoteRequest](note.md#getnoterequest) |   [NoteInfo](note.md#noteinfo) |  |
| 5 | [**list**](note.md#list)|   [NoteQuery](note.md#notequery) |   [NotesInfo](note.md#notesinfo) |  |
| 6 | [**stat**](note.md#stat)|   [NoteStatQuery](note.md#notestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | note |string|✅| |
| 3 | domain_id |string|✅| |

### GetNoteRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | note_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### NoteInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | note_id |string | |
| 2 | alert_id |string | |
| 3 | note |string | |
| 4 | created_by |string | |
| 5 | project_id |string | |
| 6 | domain_id |string | |
| 7 | created_at |string | |

### NoteQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | note_id |string|❌| |
| 3 | alert_id |string|❌| |
| 4 | created_by |string|❌| |
| 5 | project_id |string|❌| |
| 6 | domain_id |string|❌| |

### NoteRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | note_id |string|✅| |
| 2 | domain_id |string|✅| |

### NoteStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### NotesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of NoteInfo](note.md#noteinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateNoteRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | note_id |string|✅| |
| 2 | note |string|❌| |
| 3 | domain_id |string|✅| |
