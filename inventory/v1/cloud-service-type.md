---
description: A CloudServiceType is a classification with hierarchical information of `CloudService`. A CloudServiceType provides information about which `group` a specific `Resource` belongs to and which `Services` are in it.
---
# Cloud service type

>  **Package : spaceone.api.inventory.v1**

## CloudServiceType

{% hint style="info" %}
**CloudServiceType Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](cloud-service-type.md#create)|   [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |
| [**update**](cloud-service-type.md#update)|   [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |
| [**delete**](cloud-service-type.md#delete)|   [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](cloud-service-type.md#get)|   [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |
| [**list**](cloud-service-type.md#list)|   [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery) |   [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo) |
| [**stat**](cloud-service-type.md#stat)|   [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /inventory/v1/cloud-service-type/create
>

> Creates a new CloudServiceType. You must specify the `name`, `provider`, and `group` parameters to create a CloudServiceType. One or several CloudServiceTypes exist in a specific `group`, and each CloudServiceType is identified by the `name` parameter.

| Type | Message |
| :--- | :--- |
| Request | [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "API-TEST",
    "provider": "aws",
    "group": "APIGateway",
    "service_code": "AmazonApiGateway",
    "is_primary": true,
    "is_major": true,
    "resource_type": "inventory.CloudService",
    "metadata": {},
    "labels": [
        "Networking"
    ],
    "tags": {
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8",
    "name": "API-TEST",
    "provider": "aws",
    "group": "APIGateway",
    "cloud_service_type_key": "aws.APIGateway.API-TEST",
    "service_code": "AmazonApiGateway",
    "is_primary": true,
    "is_major": true,
    "resource_type": "inventory.CloudService",
    "metadata": {},
    "tags": {
        "a": "b"
    },
    "labels": [
        "Networking"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-22T01:38:16.301Z",
    "updated_at": "2022-06-22T01:38:16.301Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /inventory/v1/cloud-service-type/update
>

> Updates a specific CloudServiceType. You can make changes in CloudServiceType settings, except for `name`, `provider` and `group`. In particular, you can set the CloudServiceType's priority in a `group`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8",
    "service_code": "AmazonApi",
    "metadata": {},
    "labels": [
        "Networking2"
    ],
    "tags": {
        "b": "c"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8",
    "name": "API-TEST",
    "provider": "aws",
    "group": "APIGateway",
    "cloud_service_type_key": "aws.APIGateway.API-TEST",
    "service_code": "AmazonApi",
    "is_primary": true,
    "is_major": true,
    "resource_type": "inventory.CloudService",
    "metadata": {},
    "tags": {
        "b": "c"
    },
    "labels": [
        "Networking2"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-22T01:38:16.301Z",
    "updated_at": "2022-06-22T02:12:11.184Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /inventory/v1/cloud-service-type/delete
>

> Deletes a specific CloudServiceType. You must specify the `cloud_service_type_id` of the CloudServiceType to delete.

| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/cloud-service-type/get
>

> Gets a specific CloudServiceType. Prints detailed information about the CloudServiceType.

| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8",
    "name": "API-TEST",
    "provider": "aws",
    "group": "APIGateway",
    "cloud_service_type_key": "aws.APIGateway.API-TEST",
    "service_code": "AmazonApi",
    "is_primary": true,
    "is_major": true,
    "resource_type": "inventory.CloudService",
    "metadata": {},
    "tags": {
        "b": "c"
    },
    "labels": [
        "Networking2"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-22T01:38:16.301Z",
    "updated_at": "2022-06-22T02:12:11.184Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/cloud-service-type/list
>

> Gets a list of all CloudServiceTypes. You can use a query to get a filtered list of CloudServiceTypes.

| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery) |
| Response |  [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {
        "filter": [
            {
                "key": "provider",
                "value": "aws",
                "operator": "eq"
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
            "cloud_service_type_id": "cloud-svc-type-7e1c113b39ff",
            "name": "API",
            "provider": "aws",
            "group": "APIGateway",
            "cloud_service_type_key": "aws.APIGateway.API",
            "service_code": "AmazonApiGateway",
            "is_primary": true,
            "is_major": true,
            "resource_type": "inventory.CloudService",
            "metadata": {},
            "tags": {
                "spaceone:icon": "https://spaceone.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/Amazon-API-Gateway.svg"
            },
            "labels": [
                "Networking"
            ],
            "domain_id": "domain-58010aa2e451",
            "created_at": "2021-06-03T02:29:32.690Z",
            "updated_at": "2022-06-22T00:04:45.477Z"
        },
        {
            "cloud_service_type_id": "cloud-svc-type-64a0de601371",
            "name": "Certificate",
            "provider": "aws",
            "group": "CertificateManager",
            "cloud_service_type_key": "aws.CertificateManager.Certificate",
            "service_code": "AWSCertificateManager",
            "is_primary": true,
            "resource_type": "inventory.CloudService",
            "metadata": {},
            "tags": {
                "spaceone:icon": "https://spaceone.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/aws/AWS-Certificate-Manager.svg"
            },
            "labels": [
                "Security"
            ],
            "domain_id": "domain-58010aa2e451",
            "created_at": "2021-06-03T02:29:53.052Z",
            "updated_at": "2022-06-22T00:05:41.252Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/cloud-service-type/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CloudServiceTypeInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cloud_service_type_id |string | |
| name |string | |
| provider |string | |
| group |string | |
| cloud_service_type_key |string | |
| service_code |string | |
| is_primary |bool | |
| is_major |bool | |
| resource_type |string | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CloudServiceTypeQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| cloud_service_type_id |string|✘| |
| name |string|✘| |
| provider |string|✘| |
| group |string|✘| |
| cloud_service_type_key |string|✘| |
| service_code |string|✘| |
| is_primary |bool|✘| |
| is_major |bool|✘| |
| resource_type |string|✘| |
| domain_id |string|✔| |

### CloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✔| |
| domain_id |string|✔| |

### CloudServiceTypeStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CloudServiceTypesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| provider |string|✔| |
| group |string|✔| |
| service_code |string|✘| |
| is_primary |bool|✘| |
| is_major |bool|✘| |
| resource_type |string|✘| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✔| |
| service_code |string|✘| |
| is_primary |bool|✘| |
| is_major |bool|✘| |
| resource_type |string|✘| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
