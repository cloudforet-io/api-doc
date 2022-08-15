---
description: A CustomWidget is a widget created by a CostQuerySet a User defined.
---
# Custom widget

>  **Package : spaceone.api.cost_analysis.v1**

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
> **POST** /cost-analysis/v1/custom-widgets
>

> Creates a new CustomWidget. Based on the queries of the CostQuerySet the User made, a widget is created with the default template Cloudforet provides.

| Type | Message |
| :--- | :--- |
| Request | [CreateCustomWidgetRequest](custom-widget.md#createcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "project_provider_region-f59722cf-dc03-4758-ab7f",
    "options": {
        "group_by": "project_id",
        "stack": false,
        "layout": 100.0,
        "granularity": "ACCUMULATED",
        "filters": {},
        "chart_type": "DONUT"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "widget_id": "widget-8b1241aff67d",
    "name": "project_provider_region-f59722cf-dc03-4758-ab7f",
    "options": {
        "filters": {},
        "group_by": "project_id",
        "granularity": "ACCUMULATED",
        "layout": 100.0,
        "stack": false,
        "chart_type": "DONUT"
    },
    "tags": {},
    "user_id": "test_user@cloudforet.io",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T06:18:55.819Z",
    "updated_at": "2022-07-19T06:18:55.819Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /cost-analysis/v1/custom-widget/{widget_id}
>

> Updates a specific CustomWidget. You can make changes in CustomWidget settings, including `chart_type` and queries.

| Type | Message |
| :--- | :--- |
| Request | [UpdateCustomWidgetRequest](custom-widget.md#updatecustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "widget_id": "widget-8b1241aff67d",
    "name": "project_provider_region",
    "options": {
        "layout": 100.0,
        "chart_type": "DONUT",
        "stack": false,
        "group_by": "project_id",
        "granularity": "ACCUMULATED",
        "filters": {}
    },
    "tags": {
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "widget_id": "widget-8b1241aff67d",
    "name": "project_provider_region",
    "options": {
        "filters": {},
        "chart_type": "DONUT",
        "stack": false,
        "layout": 100.0,
        "granularity": "ACCUMULATED",
        "group_by": "project_id"
    },
    "tags": {
        "a": "b"
    },
    "user_id": "test_user@cloudforet.io",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T06:18:55.819Z",
    "updated_at": "2022-07-19T06:18:55.819Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /cost-analysis/v1/custom-widget/{widget_id}
>

> Deletes a specific CustomWidget. You must specify the `custom_widget_id` of the CustomWidget to delete.

| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetRequest](custom-widget.md#customwidgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "widget_id": "widget-205f743a9890"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/custom-widget/{widget_id}
>

> Gets a specific CustomWidget. Prints detailed information about the CustomWidget, including `chart_type` and queries.

| Type | Message |
| :--- | :--- |
| Request | [GetCustomWidgetRequest](custom-widget.md#getcustomwidgetrequest) |
| Response |  [CustomWidgetInfo](custom-widget.md#customwidgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "widget_id": "widget-205f743a9890"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "widget_id": "widget-205f743a9890",
    "name": "3 month product pie chart-a6752241-0a0b-4604-9186",
    "options": {
        "chart_type": "DONUT",
        "layout": 100.0,
        "filters": {},
        "stack": false,
        "group_by": "product",
        "granularity": "ACCUMULATED"
    },
    "tags": {},
    "user_id": "test@cloudforet.io",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-03-08T03:37:42.967Z",
    "updated_at": "2022-03-08T03:37:42.967Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/custom-widgets
>
> **POST** /cost-analysis/v1/custom-widgets/search


> Gets a list of all CustomWidgets. You can use a query to get a filtered list of CustomWidgets.

| Type | Message |
| :--- | :--- |
| Request | [CustomWidgetQuery](custom-widget.md#customwidgetquery) |
| Response |  [CustomWidgetsInfo](custom-widget.md#customwidgetsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "widget_id": "widget-205f743a9890",
            "name": "3 month product pie chart-a6752241-0a0b-4604-9186",
            "options": {
                "stack": false,
                "layout": 100.0,
                "granularity": "ACCUMULATED",
                "filters": {},
                "chart_type": "DONUT",
                "group_by": "product"
            },
            "tags": {},
            "user_id": "yuda@mz.co.kr",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-08T03:37:42.967Z",
            "updated_at": "2022-03-08T03:37:42.967Z"
        },
        {
            "widget_id": "widget-c672e1501066",
            "name": "6 month project group-589318f7-ee8d-4018-9d56",
            "options": {
                "stack": false,
                "layout": 100.0,
                "chart_type": "STACKED_COLUMN",
                "filters": {},
                "group_by": "project_group_id",
                "granularity": "MONTHLY"
            },
            "tags": {},
            "user_id": "yuda@mz.co.kr",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-14T09:30:03.115Z",
            "updated_at": "2022-03-14T09:30:03.115Z"
        }
    ],
    "total_count": 27
}
```
{% endtab %}
{% endtabs %}
 
 

 
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
| name |string|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| widget_id |string|✘| |
| name |string|✘| |
| user_id |string|✘| |
| domain_id |string|✔| |

### CustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✔| |
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
| widget_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateCustomWidgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| widget_id |string|✔| |
| name |string|✘| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
