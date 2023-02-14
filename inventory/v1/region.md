---
description: A Region is a resource storing regional information from each cloud service provider. Regional data stored by the resource includes the latitude and longitude of the region.
---
# Region

>  **Package : spaceone.api.inventory.v1**

## Region

{% hint style="info" %}
**Region Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](region.md#create)|   [CreateRegionRequest](region.md#createregionrequest) |   [RegionInfo](region.md#regioninfo) |
| [**update**](region.md#update)|   [UpdateRegionRequest](region.md#updateregionrequest) |   [RegionInfo](region.md#regioninfo) |
| [**delete**](region.md#delete)|   [RegionRequest](region.md#regionrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](region.md#get)|   [GetRegionRequest](region.md#getregionrequest) |   [RegionInfo](region.md#regioninfo) |
| [**list**](region.md#list)|   [RegionQuery](region.md#regionquery) |   [RegionsInfo](region.md#regionsinfo) |
| [**stat**](region.md#stat)|   [RegionStatQuery](region.md#regionstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /inventory/v1/region/create
>

> Creates a new Region. As the parameter `region_key`, which is automatically created when a Region is created, is in a form of `{provider}.{region_code}`, it is unique regardless of providers. You can also specify the latitude, longitude, and continent information in `tags`.

| Type | Message |
| :--- | :--- |
| Request | [CreateRegionRequest](region.md#createregionrequest) |
| Response |  [RegionInfo](region.md#regioninfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "Asia Pacific (Seoul)",
    "region_code": "ap-northeast-2",
    "provider": "aws",
    "tags": {
        "continent": "asis_pacific",
        "longitude": "73.013805",
        "latitude": "19.147428"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "region_id": "region-e41deed3c939",
    "name": "Asia Pacific (Seoul)",
    "region_key": "aws.ap-northeast-2",
    "region_code": "ap-northeast-2",
    "provider": "aws",
    "tags": {
        "continent": "asia_pacific",
        "longitude": "73.013805",
        "latitude": "19.147428"
    },
    "domain_id": "domain-x1b3c34v432",
    "created_at": "2021-11-18T13:07:31.382Z",
    "updated_at": "2022-06-17T00:07:35.469Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /inventory/v1/region/update
>

> Updates a specific Region. You can make changes in Region settings, including `name` and `tags`. The `tags` contain the continent, latitude, and longitude.

| Type | Message |
| :--- | :--- |
| Request | [UpdateRegionRequest](region.md#updateregionrequest) |
| Response |  [RegionInfo](region.md#regioninfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "region_id": "region-e41deed3c939",
    "name": "Region home",
    "tags": {
        "latitude": "6.34545",
        "continent": "asia_pacific",
        "longitude": "5.6433213"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "region_id": "region-e41deed3c939",
    "name": "Region home",
    "region_key": "aws.ap-northeast-2",
    "region_code": "ap-northeast-2",
    "provider": "aws",
    "tags": {
        "latitude": "6.34545",
        "continent": "asia_pacific",
        "longitude": "5.6433213"
    },
    "domain_id": "domain-x1b3c34v432",
    "created_at": "2021-11-18T13:07:31.382Z",
    "updated_at": "2022-06-17T00:07:35.469Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /inventory/v1/region/delete
>

> Deletes a specific Region. You must specify the `region_id` of the Region to delete.

| Type | Message |
| :--- | :--- |
| Request | [RegionRequest](region.md#regionrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "region_id": "region-e41deed3c939"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/region/get
>

> Gets a specific Region. Prints detailed information about the Region, including `name`, `region_code`, and a location coordinate.

| Type | Message |
| :--- | :--- |
| Request | [GetRegionRequest](region.md#getregionrequest) |
| Response |  [RegionInfo](region.md#regioninfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "region_id": "region-f803eb00b567"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "region_id": "region-f803eb00b567",
    "name": "Asia Pacific (Seoul)",
    "region_key": "aws.ap-northeast-2",
    "region_code": "ap-northeast-2",
    "provider": "aws",
    "tags": {
        "latitude": "6.34545",
        "continent": "asia_pacific",
        "longitude": "5.6433213"
    },
    "domain_id": "domain-x1b3c34v432",
    "created_at": "2022-03-21T09:08:31.961Z",
    "updated_at": "2022-06-17T00:07:35.749Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/region/list
>

> Gets a list of all Regions. You can use a query to get a filtered list of Regions.

| Type | Message |
| :--- | :--- |
| Request | [RegionQuery](region.md#regionquery) |
| Response |  [RegionsInfo](region.md#regionsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {
        "filter": [
            {
                "key": "name",
                "value": "Asia Pacific",
                "operator": "contain"
            }
        ]
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "region_id": "region-e41deed3c939",
            "name": "Asia Pacific (Mumbai)",
            "region_key": "aws.ap-south-1",
            "region_code": "ap-south-1",
            "provider": "aws",
            "tags": {
                "continent": "asia_pacific",
                "longitude": "73.013805",
                "latitude": "19.147428"
            },
            "domain_id": "domain-x1b3c34v432",
            "created_at": "2021-11-18T13:07:31.382Z",
            "updated_at": "2022-06-17T00:07:35.469Z"
        },
        {
            "region_id": "region-f803eb00b567",
            "name": "Asia Pacific (Seoul)",
            "region_key": "aws.ap-northeast-2",
            "region_code": "ap-northeast-2",
            "provider": "aws",
            "tags": {
                "latitude": "6.34545",
                "continent": "asia_pacific",
                "longitude": "5.6433213"
            },
            "domain_id": "domain-x1b3c34v432",
            "created_at": "2022-03-21T09:08:31.961Z",
            "updated_at": "2022-06-17T00:07:35.749Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/region/stat
>


| Type | Message |
| :--- | :--- |
| Request | [RegionStatQuery](region.md#regionstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateRegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| region_code |string|✔| |
| provider |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetRegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| region_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### RegionInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| region_id |string | |
| name |string | |
| region_key |string | |
| region_code |string | |
| provider |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### RegionQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| region_id |string|✘| |
| name |string|✘| |
| region_key |string|✘| |
| region_code |string|✘| |
| provider |string|✘| |
| domain_id |string|✔| |

### RegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| region_id |string|✔| |
| domain_id |string|✔| |

### RegionStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### RegionsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RegionInfo](region.md#regioninfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateRegionRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| region_id |string|✔| |
| name |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
