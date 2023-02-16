---
description: A Quota is a limit on protocol usage for a day or a month. You can manage the use of the protocol with a Quota.
---
# Quota

>  **Package : spaceone.api.notification.v1**

## Quota

{% hint style="info" %}
**Quota Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](quota.md#create)|   [CreateQuotaRequest](quota.md#createquotarequest) |   [QuotaInfo](quota.md#quotainfo) |
| [**update**](quota.md#update)|   [UpdateQuotaRequest](quota.md#updatequotarequest) |   [QuotaInfo](quota.md#quotainfo) |
| [**delete**](quota.md#delete)|   [QuotaRequest](quota.md#quotarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](quota.md#get)|   [QuotaRequest](quota.md#quotarequest) |   [QuotaInfo](quota.md#quotainfo) |
| [**list**](quota.md#list)|   [QuotaQuery](quota.md#quotaquery) |   [QuotasInfo](quota.md#quotasinfo) |
| [**stat**](quota.md#stat)|   [QuotaStatQuery](quota.md#quotastatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /notification/v1/quota/create
>

> Creates a new Quota limiting the use of a selected Protocol for a day or a month. If the parameter `limit` has no value, it will be deemed unlimited. If a Protocol has not set a Quota, the default Quota set in the Config will be applied.

| Type | Message |
| :--- | :--- |
| Request | [CreateQuotaRequest](quota.md#createquotarequest) |
| Response |  [QuotaInfo](quota.md#quotainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "protocol_id": "protocol-123456789012",
    "limit": {
        "day": 5.0,
        "month": 7.0
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "quota_id": "quota-123456789012",
    "protocol_id": "protocol-123456789012",
    "limit": {
        "day": 5.0,
        "month": 7.0
    },
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /notification/v1/quota/update
>

> Updates a specific Quota. You can make changes in Quota `limit`, managing the use of the Protocol.

| Type | Message |
| :--- | :--- |
| Request | [UpdateQuotaRequest](quota.md#updatequotarequest) |
| Response |  [QuotaInfo](quota.md#quotainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "quota_id": "quota-123456789012",
    "limit": {
        "day": 10.0,
        "month": 15.0
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "quota_id": "quota-123456789012",
    "protocol_id": "protocol-123456789012",
    "limit": {
        "day": 10.0,
        "month": 15.0
    },
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /notification/v1/quota/delete
>

> Deletes a specific Quota. The default Quota set in the Config will be applied to the Protocol you deleted the Quota of.

| Type | Message |
| :--- | :--- |
| Request | [QuotaRequest](quota.md#quotarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "quota_id": "quota-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /notification/v1/quota/get
>

> Gets a specific Quota. Prints detailed information about the Quota, including the `limit` and the Protocol limited by the Quota.

| Type | Message |
| :--- | :--- |
| Request | [QuotaRequest](quota.md#quotarequest) |
| Response |  [QuotaInfo](quota.md#quotainfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "quota_id": "quota-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "quota_id": "quota-123456789012",
    "protocol_id": "protocol-123456789012",
    "limit": {
        "day": 10.0,
        "month": 15.0
    },
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /notification/v1/quota/list
>

> Gets a list of all Quotas. You can use a query to get a filtered list of Quotas.

| Type | Message |
| :--- | :--- |
| Request | [QuotaQuery](quota.md#quotaquery) |
| Response |  [QuotasInfo](quota.md#quotasinfo)  |
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
            "quota_id": "quota-123456789012",
            "protocol_id": "protocol-123456789012",
            "limit": {
                "day": 10.0,
                "month": 15.0
            },
            "domain_id": "domain-123456789012"
        },
        {
            "quota_id": "quota-987654321098",
            "protocol_id": "protocol-987654321098",
            "limit": {
                "day": 5.0,
                "month": 7.0
            },
            "domain_id": "domain-123456789012"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /notification/v1/quota/stat
>


| Type | Message |
| :--- | :--- |
| Request | [QuotaStatQuery](quota.md#quotastatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateQuotaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✔| |
| limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| The information about Quota limitation.|
| domain_id |string|✔| The ID of domain.|

### QuotaInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| quota_id |string | The ID of Quota.|
| protocol_id |string | The ID of Protocol.|
| limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | The information about Quota limitation.|
| domain_id |string | The ID of domain|

### QuotaQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| Query format provided by SpaceONE. Please check the link for more information.|
| quota_id |string|✘| The ID of Quota.|
| protocol_id |string|✘| The ID of Protocol.|
| domain_id |string|✔| The ID of domain.|

### QuotaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| quota_id |string|✔| The ID of Quota.|
| domain_id |string|✔| The ID of domain.|

### QuotaStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✔| The ID of domain.|

### QuotasInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of QuotaInfo](quota.md#quotainfo) | List of queried Quota.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Quota.|

### UpdateQuotaRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| quota_id |string|✔| The ID of Quota.|
| limit |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| The information about Quota limitation.|
| domain_id |string|✔| |
