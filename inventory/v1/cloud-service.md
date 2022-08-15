---
description: A CloudService is data of an `instance` of a `resource`. A CloudService follows the pre-created classification system of a CloudServiceType and indicates the property value of the `resource`.
---
# Cloud service

>  **Package : spaceone.api.inventory.v1**

## CloudService

{% hint style="info" %}
**CloudService Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](cloud-service.md#create)|   [CreateServiceRequest](cloud-service.md#createservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |
| [**update**](cloud-service.md#update)|   [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |
| [**delete**](cloud-service.md#delete)|   [CloudServiceRequest](cloud-service.md#cloudservicerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](cloud-service.md#get)|   [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |
| [**list**](cloud-service.md#list)|   [CloudServiceQuery](cloud-service.md#cloudservicequery) |   [CloudServicesInfo](cloud-service.md#cloudservicesinfo) |
| [**stat**](cloud-service.md#stat)|   [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /inventory/v1/cloud-services
>

> Creates a new CloudService. A CloudService instance is created based on data including the `resource`'s attribute values. When creating, the classification information defined by CloudServiceType is also needed. The created CloudService has collection information which is the collection history for the `resource` by plugin.

| Type | Message |
| :--- | :--- |
| Request | [CreateServiceRequest](cloud-service.md#createservicerequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cloud_service_type": "Key",
    "provider": "aws",
    "cloud_service_group": "KMS",
    "name": "cloud_service_test",
    "account": "251340636361",
    "launched_at": "2020-08-03T15:00:54.000Z",
    "ip_addresses": [],
    "data": {
        "alias_arn": null,
        "origin": "AWS_KMS",
        "cloudwatch": {
            "region_name": "ap-northeast-1",
            "namespace": "AWS/KMS",
            "dimensions": [
                {
                    "Value": "0drda5e1-c40f-45d7-a647-xxxxxxx",
                    "Name": "KeyId"
                }
            ]
        },
        "aws_account_id": "251340636361",
        "creation_date": "2020-07-09T09:39:03.097000+0000",
        "encryption_algorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "key_usage": "ENCRYPT_DECRYPT",
        "key_id": "0drda5e1-c40f-45d7-a647-xxxxxxx",
        "key_type_path": "defaultKeys",
        "key_rotated": false,
        "description": "Default master key that protects my Secrets Manager data when no other key is defined",
        "key_state": "Enabled",
        "customer_master_key_spec": "SYMMETRIC_DEFAULT",
        "enabled": true,
        "arn": "arn:aws:kms:ap-northeast-1:251340636361:key/0drda5e1-c40f-45d7-a647-xxxxxxx",
        "key_manager": "AWS"
    },
    "metadata": {},
    "reference": {
        "resource_id": "arn:aws:kms:ap-northeast-1:251340636361:key/0drda5e1-c40f-45d7-a647-xxxxxxx",
        "external_link": "https://console.aws.amazon.com/kms/home?region=ap-northeast-1#/kms/defaultKeys/0drda5e1-c40f-45d7-a647-xxxxxxx/"
    },
    "tags": {
        "a": "b"
    },
    "region_code": "ap-northeast-1"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cloud_service_id": "cloud-svc-c00f38a173e1",
    "name": "cloud_service_test",
    "state": "ACTIVE",
    "account": "251340636361",
    "cloud_service_type": "Key",
    "cloud_service_group": "KMS",
    "provider": "aws",
    "data": {
        "alias_arn": null,
        "origin": "AWS_KMS",
        "cloudwatch": {
            "region_name": "ap-northeast-1",
            "namespace": "AWS/KMS",
            "dimensions": [
                {
                    "Value": "0drda5e1-c40f-45d7-a647-xxxxxxx",
                    "Name": "KeyId"
                }
            ]
        },
        "aws_account_id": "251340636361",
        "creation_date": "2020-07-09T09:39:03.097000+0000",
        "encryption_algorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "key_usage": "ENCRYPT_DECRYPT",
        "key_id": "0drda5e1-c40f-45d7-a647-xxxxxxx",
        "key_type_path": "defaultKeys",
        "key_rotated": false,
        "description": "Default master key that protects my Secrets Manager data when no other key is defined",
        "key_state": "Enabled",
        "customer_master_key_spec": "SYMMETRIC_DEFAULT",
        "enabled": true,
        "arn": "arn:aws:kms:ap-northeast-1:251340636361:key/0drda5e1-c40f-45d7-a647-xxxxxxx",
        "key_manager": "AWS"
    },
    "metadata": {
        "manual": {}
    },
    "reference": {
        "resource_id": "arn:aws:kms:ap-northeast-1:251340636361:key/0drda5e1-c40f-45d7-a647-xxxxxxx",
        "external_link": "https://console.aws.amazon.com/kms/home?region=ap-northeast-1#/kms/defaultKeys/0drda5e1-c40f-45d7-a647-xxxxxxx/"
    },
    "tags": {
        "a": "b"
    },
    "collection_info": {
        "collectors": [],
        "service_accounts": [],
        "secrets": []
    },
    "ip_addresses": [],
    "region_code": "ap-northeast-1",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-22T06:38:48.989Z",
    "updated_at": "2022-06-22T06:38:48.989Z",
    "launched_at": "2020-08-03T15:00:54.000Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /inventory/v1/cloud-service/{cloud_service_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/cloud-service/{cloud_service_id}
>

> Deletes a specific CloudService. You must specify the `cloud_service_id` of the CloudService to delete.

| Type | Message |
| :--- | :--- |
| Request | [CloudServiceRequest](cloud-service.md#cloudservicerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cloud_service_id": "cloud-svc-fea2b0d32141"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /inventory/v1/cloud-service/{cloud_service_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
 
 

 
### list
> **GET** /inventory/v1/cloud-services
>
> **POST** /inventory/v1/cloud-services/search



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceQuery](cloud-service.md#cloudservicequery) |
| Response |  [CloudServicesInfo](cloud-service.md#cloudservicesinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/cloud-services/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CloudServiceInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cloud_service_id |string | |
| name |string | |
| state |string | |
| account |string | |
| instance_type |string | |
| instance_size |float | |
| cloud_service_type |string | |
| cloud_service_group |string | |
| provider |string | |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| reference |[CloudServiceReference](cloud-service.md#cloudservicereference) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| ip_addresses |list of string | |
| region_code |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |
| deleted_at |string | |

### CloudServiceQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| cloud_service_id |string|✘| |
| name |string|✘| |
| state |string|✘| |
| account |string|✘| |
| instance_type |string|✘| |
| cloud_service_type |string|✘| |
| cloud_service_group |string|✘| |
| provider |string|✘| |
| region_code |string|✘| |
| ip_address |string|✘| |
| resource_group_id |string|✘| |
| project_id |string|✘| |
| project_group_id |string|✘| |
| domain_id |string|✔| |

### CloudServiceReference
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| external_link |string | |

### CloudServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✔| |
| domain_id |string|✔| |

### CloudServiceStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |
| resource_group_id |string|✘| |

### CloudServicesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CloudServiceInfo](cloud-service.md#cloudserviceinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type |string|✔| |
| provider |string|✔| |
| cloud_service_group |string|✔| |
| name |string|✘| |
| account |string|✘| |
| instance_type |string|✘| |
| instance_size |float|✘| |
| ip_addresses |list of string|✘| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| reference |[CloudServiceReference](cloud-service.md#cloudservicereference)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| region_code |string|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |

### GetCloudServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### PinCloudServiceDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✔| |
| keys |list of string|✔| |
| domain_id |string|✔| |

### UpdateCloudServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✔| |
| name |string|✘| |
| account |string|✘| |
| instance_type |string|✘| |
| instance_size |float|✘| |
| ip_addresses |list of string|✘| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| reference |[CloudServiceReference](cloud-service.md#cloudservicereference)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| region_code |string|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |
| release_project |bool|✘| |
| release_region |bool|✘| |
