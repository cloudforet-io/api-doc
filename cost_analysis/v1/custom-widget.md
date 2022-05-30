---
description:  
---
# Custom widget

>  **Package : spaceone.api.cost_analysis.v1**

## CustomWidget

{% hint style="info" %}
**CustomWidget Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**create**](custom-widget.md#create)|   [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |
| [**update**](custom-widget.md#update)|   [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |
| [**delete**](custom-widget.md#delete)|   [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](custom-widget.md#get)|   [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |
| [**list**](custom-widget.md#list)|   [CustomWidgetQuery](custom-widget.md#customwidgetquery) |   [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo) |
| [**stat**](custom-widget.md#stat)|   [CustomWidgetStatQuery](custom-widget.md#customwidgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/custom-widgets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/custom-widget/{widget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/custom-widget/{widget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/custom-widget/{widget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/custom-widgets
>
> **POST** /cost-analysis/v1/custom-widgets/search



| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetQuery](custom-widget.md#customwidgetquery) |
| Response |  [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/custom-widgets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetStatQuery](custom-widget.md#customwidgetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### CustomWidgetInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| widget_id |string | |
| name |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| user_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CustomWidgetQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| widget_id |string|❌| |
| name |string|❌| |
| user_id |string|❌| |
| domain_id |string|✅| |

### CustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✅| |
| domain_id |string|✅| |

### CustomWidgetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CustomWidgetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CustomWidgetInfo](custom-widget.md#customwidgetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✅| |
| name |string|❌| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
