---
description: A Trusted Secret is an external data, encrypted by CloudForet.
---
# Trusted secret

>  **Package : spaceone.api.secret.v1**

## TrustedSecret

{% hint style="info" %}
**TrustedSecret Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](trusted-secret.md#create)|   [CreateTrustedSecretRequest](trusted-secret.md#createtrustedsecretrequest) |   [TrustedSecretInfo](trusted-secret.md#trustedsecretinfo) |
| [**update**](trusted-secret.md#update)|   [UpdateTrustedSecretRequest](trusted-secret.md#updatetrustedsecretrequest) |   [TrustedSecretInfo](trusted-secret.md#trustedsecretinfo) |
| [**delete**](trusted-secret.md#delete)|   [TrustedSecretRequest](trusted-secret.md#trustedsecretrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**update_data**](trusted-secret.md#update_data)|   [UpdateTrustedSecretDataRequest](trusted-secret.md#updatetrustedsecretdatarequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](trusted-secret.md#get)|   [GetTrustedSecretRequest](trusted-secret.md#gettrustedsecretrequest) |   [TrustedSecretInfo](trusted-secret.md#trustedsecretinfo) |
| [**list**](trusted-secret.md#list)|   [TrustedSecretQuery](trusted-secret.md#trustedsecretquery) |   [TrustedSecretsInfo](trusted-secret.md#trustedsecretsinfo) |
| [**stat**](trusted-secret.md#stat)|   [TrustedSecretStatQuery](trusted-secret.md#trustedsecretstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /secret/v1/trusted-secret/create
>

> Creates a new Trusted Secret. When creating the resource, external `data` is encrypted, and a `trusted_secret_id` is issued for data access by other microservices.

| Type | Message |
| :--- | :--- |
| Request | [CreateTrustedSecretRequest](trusted-secret.md#createtrustedsecretrequest) |
| Response |  [TrustedSecretInfo](trusted-secret.md#trustedsecretinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "aws-dev",
    "data": "********",
    "schema": "aws_access_key",
    "service_account_id": "sa-123456789012",
    "tags": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "name": "aws-dev",
    "tags": {},
    "schema": "aws_access_key",
    "provider": "aws",
    "service_account_id": "sa-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:10:14.851Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /secret/v1/trusted-secret/update
>

> Updates a specific Secret. You can make changes in Secret settings, including `name` and`tags`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateTrustedSecretRequest](trusted-secret.md#updatetrustedsecretrequest) |
| Response |  [TrustedSecretInfo](trusted-secret.md#trustedsecretinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "name": "aws-dev2",
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "name": "aws-dev2",
    "tags": {
        "a": "b"
    },
    "schema": "aws_access_key",
    "provider": "aws",
    "service_account_id": "sa-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:10:14.851Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /secret/v1/trusted-secret/delete
>

> Deletes a specific Secret. You must specify the `secret_id` of the Secret to delete.

| Type | Message |
| :--- | :--- |
| Request | [TrustedSecretRequest](trusted-secret.md#trustedsecretrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update_data
> **POST** /secret/v1/trusted-secret/update-data
>

> Updates encrypted data of a specific Secret resource. For example, to change the parameter `data`, external data to encrypt, you can use `update_data` to create new encrypted data based on the changed `data` and store it in the Secret resource.

| Type | Message |
| :--- | :--- |
| Request | [UpdateTrustedSecretDataRequest](trusted-secret.md#updatetrustedsecretdatarequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "data": "********",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data": {
        "encrypted_data": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    },
    "encrypted": true,
    "encrypt_options": {
        "encrypted_data_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "encrypt_algorithm": "CloudForet_DEFAULT"
    }
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /secret/v1/trusted-secret/get
>

> Gets a specific Post. You must specify the `post_id` of the Post to get, and the `board_id` of the Board where the child Post to get belongs. Prints detailed information about the Post.

| Type | Message |
| :--- | :--- |
| Request | [GetTrustedSecretRequest](trusted-secret.md#gettrustedsecretrequest) |
| Response |  [TrustedSecretInfo](trusted-secret.md#trustedsecretinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "trusted_secret_id": "trusted-secret-123456789012",
    "name": "aws-dev",
    "tags": {},
    "schema": "aws_access_key",
    "provider": "aws",
    "service_account_id": "sa-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:10:14.851Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /secret/v1/trusted-secret/list
>

> Gets a list of all Posts. You can use a query to get a filtered list of Posts.

| Type | Message |
| :--- | :--- |
| Request | [TrustedSecretQuery](trusted-secret.md#trustedsecretquery) |
| Response |  [TrustedSecretsInfo](trusted-secret.md#trustedsecretsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "trusted_secret_id": "trusted-secret-123456789012",
            "name": "aws-dev",
            "tags": {},
            "schema": "aws_access_key",
            "provider": "aws",
            "service_account_id": "sa-123456789012",
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T06:10:14.851Z"
        },
        {
            "trusted_secret_id": "trusted-secret-987654321098",
            "name": "plugin-credentials",
            "tags": {},
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T02:31:01.709Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /secret/v1/trusted-secret/stat
>


| Type | Message |
| :--- | :--- |
| Request | [TrustedSecretStatQuery](trusted-secret.md#trustedsecretstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateTrustedSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| schema |string|✘| |
| service_account_id |string|✘| |
| domain_id |string|✔| |

### GetTrustedSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| trusted_secret_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### TrustedSecretInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| trusted_secret_id |string | |
| name |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| schema |string | |
| provider |string | |
| service_account_id |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |

### TrustedSecretQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| trusted_secret_id |string|✘| |
| name |string|✘| |
| schema |string|✘| |
| provider |string|✘| |
| service_account_id |string|✘| |
| domain_id |string|✔| |

### TrustedSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| trusted_secret_id |string|✔| |
| domain_id |string|✔| |

### TrustedSecretStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### TrustedSecretsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of TrustedSecretInfo](trusted-secret.md#trustedsecretinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateTrustedSecretDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| trusted_secret_id |string|✔| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| schema |string|✘| |
| domain_id |string|✔| |

### UpdateTrustedSecretRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| trusted_secret_id |string|✔| |
| name |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
