---
description: description of dashboard
---
# Custom widget

>  **Package : spaceone.api.dashboard.v1**

## CustomWidget

{% hint style="info" %}
**CustomWidget Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](custom-widget.md#create)|   [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |
| [**update**](custom-widget.md#update)|   [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |
| [**delete**](custom-widget.md#delete)|   [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](custom-widget.md#get)|   [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |   [CustomWidgetInfo](custom-widget.md#customwidgetinfo) |
| [**list**](custom-widget.md#list)|   [CustomWidgetQuery](custom-widget.md#customwidgetquery) |   [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo) |
| [**stat**](custom-widget.md#stat)|   [CustomWidgetStatQuery](custom-widget.md#customwidgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /dashboard/v1/custom-widget/create
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### update
> **POST** /dashboard/v1/custom-widget/update
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### delete
> **POST** /dashboard/v1/custom-widget/delete
>


| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /dashboard/v1/custom-widget/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
 
 

 
### list
> **POST** /dashboard/v1/custom-widget/list
>


| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetQuery](custom-widget.md#customwidgetquery) |
| Response |  [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo)  |
 
 

 
### stat
> **POST** /dashboard/v1/custom-widget/stat
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
| widget_name |string|✔| |
| title |string|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| inherit_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### CustomWidgetInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| custom_widget_id |string | |
| widget_name |string | |
| title |string | |
| version |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| inherit_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| user_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CustomWidgetQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| custom_widget_id |string|✘| |
| widget_name |string|✘| |
| title |string|✘| |
| user_id |string|✘| |
| domain_id |string|✔| |

### CustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| custom_widget_id |string|✔| |
| domain_id |string|✔| |

### CustomWidgetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CustomWidgetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CustomWidgetInfo](custom-widget.md#customwidgetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| custom_widget_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| custom_widget_id |string|✔| |
| title |string|✘| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| settings |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| inherit_options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
