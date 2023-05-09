---
title: "Cloud_service_type"
linkTitle: "Cloud_service_type"
weight: 3
bookFlatSection: true
---
# [Cloud_service_type](#Cloud_service_type)
desc: A CloudServiceType is a classification with hierarchical information of `CloudService`. A CloudServiceType provides information about which `group` a specific `Resource` belongs to and which `Services` are in it.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Cloud_service_type





**CloudServiceType Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudServiceType#create) | [CreateCloudServiceTypeRequest](CloudServiceType#createcloudservicetyperequest) | [CloudServiceTypeInfo](./CloudServiceType#cloudservicetypeinfo) |
| [**update**](./CloudServiceType#update) | [UpdateCloudServiceTypeRequest](CloudServiceType#updatecloudservicetyperequest) | [CloudServiceTypeInfo](./CloudServiceType#cloudservicetypeinfo) |
| [**delete**](./CloudServiceType#delete) | [CloudServiceTypeRequest](CloudServiceType#cloudservicetyperequest) | [Empty](./CloudServiceType#empty) |
| [**get**](./CloudServiceType#get) | [GetCloudServiceTypeRequest](CloudServiceType#getcloudservicetyperequest) | [CloudServiceTypeInfo](./CloudServiceType#cloudservicetypeinfo) |
| [**list**](./CloudServiceType#list) | [CloudServiceTypeQuery](CloudServiceType#cloudservicetypequery) | [CloudServiceTypesInfo](./CloudServiceType#cloudservicetypesinfo) |
| [**stat**](./CloudServiceType#stat) | [CloudServiceTypeStatQuery](CloudServiceType#cloudservicetypestatquery) | [Struct](./CloudServiceType#struct) |



    
<br>

### create

desc: Creates a new CloudServiceType. You must specify the `name`, `provider`, and `group` parameters to create a CloudServiceType. One or several CloudServiceTypes exist in a specific `group`, and each CloudServiceType is identified by the `name` parameter.
request_example: >-
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
response_example: >-
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



> **POST** /inventory/v1/cloud-service-type/create
>






    
<br>

### update

desc: Updates a specific CloudServiceType. You can make changes in CloudServiceType settings, except for `name`, `provider` and `group`. In particular, you can set the CloudServiceType's priority in a `group`.
request_example: >-
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
response_example: >-
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



> **POST** /inventory/v1/cloud-service-type/update
>






    
<br>

### delete

desc: Deletes a specific CloudServiceType. You must specify the `cloud_service_type_id` of the CloudServiceType to delete.
request_example: >-
{
"cloud_service_type_id": "cloud-svc-type-27dd73ac89f8"
}



> **POST** /inventory/v1/cloud-service-type/delete
>






    
<br>

### get

desc: Gets a specific CloudServiceType. Prints detailed information about the CloudServiceType.
request_example: >-
{
"cloud_service_type_id": "cloud-svc-type-27dd73ac89f8"
}
response_example: >-
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



> **POST** /inventory/v1/cloud-service-type/get
>






    
<br>

### list

desc: Gets a list of all CloudServiceTypes. You can use a query to get a filtered list of CloudServiceTypes.
request_example: >-
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
response_example: >-
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
"metadata": {
},
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
"metadata": {
},
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



> **POST** /inventory/v1/cloud-service-type/list
>






    
<br>

### stat





> **POST** /inventory/v1/cloud-service-type/stat
>






    


<br>
<br>

## Message



### CloudServiceTypeInfo
* **cloud_service_type_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **group** (string)  `Required` 

    
* **cloud_service_type_key** (string)  `Required` 

    
* **service_code** (string)  `Required` 

    
* **is_primary** (bool)  `Required` 

    
* **is_major** (bool)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### CloudServiceTypeQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **cloud_service_type_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **group** (string)  `Required` 

  *is_required: false*

    
* **cloud_service_type_key** (string)  `Required` 

  *is_required: false*

    
* **service_code** (string)  `Required` 

  *is_required: false*

    
* **is_primary** (bool)  `Required` 

  *is_required: false*

    
* **is_major** (bool)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceTypeRequest
* **cloud_service_type_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceTypeStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceTypesInfo
* **results** (CloudServiceTypeInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCloudServiceTypeRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: true*

    
* **group** (string)  `Required` 

  *is_required: true*

    
* **service_code** (string)  `Required` 

  *is_required: false*

    
* **is_primary** (bool)  `Required` 

  *is_required: false*

    
* **is_major** (bool)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetCloudServiceTypeRequest
* **cloud_service_type_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateCloudServiceTypeRequest
* **cloud_service_type_id** (string)  `Required` 

  *is_required: true*

    
* **service_code** (string)  `Required` 

  *is_required: false*

    
* **is_primary** (bool)  `Required` 

  *is_required: false*

    
* **is_major** (bool)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
