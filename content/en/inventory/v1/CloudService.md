---
title: "CloudService"
linkTitle: "CloudService"
weight: 3
bookFlatSection: true
---
# [CloudService](#CloudService)
A CloudService is data of an `instance` of a `resource`. A CloudService follows the pre-created classification system of a CloudServiceType and indicates the property value of the `resource`.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## CloudService





**CloudService Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudService#create) | [CreateServiceRequest](CloudService#createservicerequest) | [CloudServiceInfo](CloudService#cloudserviceinfo) |
| [**update**](./CloudService#update) | [UpdateCloudServiceRequest](CloudService#updatecloudservicerequest) | [CloudServiceInfo](CloudService#cloudserviceinfo) |
| [**delete**](./CloudService#delete) | [CloudServiceRequest](CloudService#cloudservicerequest) | [Empty](CloudService#empty) |
| [**get**](./CloudService#get) | [GetCloudServiceRequest](CloudService#getcloudservicerequest) | [CloudServiceInfo](CloudService#cloudserviceinfo) |
| [**list**](./CloudService#list) | [CloudServiceQuery](CloudService#cloudservicequery) | [CloudServicesInfo](CloudService#cloudservicesinfo) |
| [**export**](./CloudService#export) | [CloudServiceExportRequest](CloudService#cloudserviceexportrequest) | [Struct](CloudService#struct) |
| [**analyze**](./CloudService#analyze) | [CloudServiceAnalyzeQuery](CloudService#cloudserviceanalyzequery) | [Struct](CloudService#struct) |
| [**stat**](./CloudService#stat) | [CloudServiceStatQuery](CloudService#cloudservicestatquery) | [Struct](CloudService#struct) |



    
<br>

### create

Creates a new CloudService. A CloudService instance is created based on data including the `resource`'s attribute values. When creating, the classification information defined by CloudServiceType is also needed. The created CloudService has collection information which is the collection history for the `resource` by plugin.



> **POST** /inventory/v1/cloud-service/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateServiceRequest](./CloudService#createservicerequest)

* **cloud_service_type** (string)   `Required` 


* **provider** (string)   `Required` 


* **cloud_service_group** (string)   `Required` 


* **data** (Struct)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **account** (string)  


* **instance_type** (string)  


* **instance_size** (float)  


* **ip_addresses** (string)  `Repeated`   


* **metadata** (Struct)  


* **reference** (CloudServiceReference)  


* **tags** (Struct)  


* **region_code** (string)  


* **project_id** (string)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceInfo](#CLOUDSERVICEINFO)
* **cloud_service_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (string)   `Required` 

* **account** (string)   `Required` 

* **instance_type** (string)   `Required` 

* **instance_size** (float)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **provider** (string)   `Required` 

* **data** (Struct)   `Required` 

* **metadata** (Struct)   `Required` 

* **reference** (CloudServiceReference)   `Required` 

* **tags** (Struct)   `Required` 

* **tag_keys** (Struct)   `Required` 

* **collection_info** (CollectionInfo)  `Repeated`   `Required` 

* **ip_addresses** (string)  `Repeated`   `Required` 

* **region_code** (string)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific CloudService. You can make changes in CloudService settings, except for the classification system of CloudService and the information about the `resource` attribute value.



> **POST** /inventory/v1/cloud-service/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateCloudServiceRequest](./CloudService#updatecloudservicerequest)

* **cloud_service_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **account** (string)  


* **instance_type** (string)  


* **instance_size** (float)  


* **ip_addresses** (string)  `Repeated`   


* **data** (Struct)  


* **metadata** (Struct)  


* **reference** (CloudServiceReference)  


* **tags** (Struct)  


* **region_code** (string)  


* **project_id** (string)  


* **release_project** (bool)  


* **release_region** (bool)  





{{< highlight json >}}
{
   "cloud_service_id": "cloud-svc-c00f38a173e1",
   "name": "cloud_service_test2",
   "ip_addresses": [
       "1.1.1.1",
       "2.2.2.2"
   ],
   "tags": {
       "description": "spaceone"
   },
   "region_code": "ap-northeast-2"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceInfo](#CLOUDSERVICEINFO)
* **cloud_service_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (string)   `Required` 

* **account** (string)   `Required` 

* **instance_type** (string)   `Required` 

* **instance_size** (float)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **provider** (string)   `Required` 

* **data** (Struct)   `Required` 

* **metadata** (Struct)   `Required` 

* **reference** (CloudServiceReference)   `Required` 

* **tags** (Struct)   `Required` 

* **tag_keys** (Struct)   `Required` 

* **collection_info** (CollectionInfo)  `Repeated`   `Required` 

* **ip_addresses** (string)  `Repeated`   `Required` 

* **region_code** (string)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific CloudService. You must specify the `cloud_service_id` of the CloudService to delete.



> **POST** /inventory/v1/cloud-service/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CloudServiceRequest](./CloudService#cloudservicerequest)

* **cloud_service_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "cloud_service_id": "cloud-svc-fea2b0d32141"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific CloudService. Prints detailed information about the CloudService, including its state, classification information, and attribute values.



> **POST** /inventory/v1/cloud-service/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetCloudServiceRequest](./CloudService#getcloudservicerequest)

* **cloud_service_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "cloud_service_id": "cloud-svc-fea2b0d32141"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceInfo](#CLOUDSERVICEINFO)
* **cloud_service_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (string)   `Required` 

* **account** (string)   `Required` 

* **instance_type** (string)   `Required` 

* **instance_size** (float)   `Required` 

* **cloud_service_type** (string)   `Required` 

* **cloud_service_group** (string)   `Required` 

* **provider** (string)   `Required` 

* **data** (Struct)   `Required` 

* **metadata** (Struct)   `Required` 

* **reference** (CloudServiceReference)   `Required` 

* **tags** (Struct)   `Required` 

* **tag_keys** (Struct)   `Required` 

* **collection_info** (CollectionInfo)  `Repeated`   `Required` 

* **ip_addresses** (string)  `Repeated`   `Required` 

* **region_code** (string)   `Required` 

* **project_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all CloudServices. You can use a query to get a filtered list of CloudServices.



> **POST** /inventory/v1/cloud-service/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CloudServiceQuery](./CloudService#cloudservicequery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **cloud_service_id** (string)  


* **name** (string)  


* **state** (string)  


* **account** (string)  


* **instance_type** (string)  


* **cloud_service_type** (string)  


* **cloud_service_group** (string)  


* **provider** (string)  


* **region_code** (string)  


* **ip_address** (string)  


* **project_id** (string)  


* **project_group_id** (string)  





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "cloud_service_type",
               "value": "Key",
               "operator": "eq"
           }
       ]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServicesInfo](#CLOUDSERVICESINFO)
* **results** (CloudServiceInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [{
       "cloud_service_id": "cloud-svc-c00f38a173e1",
       "name": "cloud_service_test2",
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
           "description": "spaceone"
       },
       "collection_info": {
           "collectors": [],
           "service_accounts": [],
           "secrets": []
       },
       "ip_addresses": [
           "1.1.1.1",
           "2.2.2.2"
       ],
       "region_code": "ap-northeast-1",
       "domain_id": "domain-58010aa2e451",
       "created_at": "2022-06-22T06:38:48.989Z",
       "updated_at": "2022-06-22T06:38:48.989Z",
       "launched_at": "2020-08-03T15:00:54.000Z"
   }],
   "total_count": 1
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### export





> **POST** /inventory/v1/cloud-service/export
>






    
<br>

### analyze





> **POST** /inventory/v1/cloud-service/analyze
>






    
<br>

### stat





> **POST** /inventory/v1/cloud-service/stat
>






    


<br>
<br>

## Message



### CloudServiceAnalyzeQuery
* **query** (AnalyzeQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CloudServiceExportRequest
* **options** (ExportOption)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **file_format** (FileFormat)  

    
* **file_name** (string)  

    
* **timezone** (string)  

    <br>

### CloudServiceInfo
* **cloud_service_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (string)   `Required` 

    
* **account** (string)   `Required` 

    
* **instance_type** (string)   `Required` 

    
* **instance_size** (float)   `Required` 

    
* **cloud_service_type** (string)   `Required` 

    
* **cloud_service_group** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **reference** (CloudServiceReference)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **tag_keys** (Struct)   `Required` 

    
* **collection_info** (CollectionInfo)  `Repeated`    `Required` 

    
* **ip_addresses** (string)  `Repeated`    `Required` 

    
* **region_code** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    <br>

### CloudServiceQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **cloud_service_id** (string)  

    
* **name** (string)  

    
* **state** (string)  

    
* **account** (string)  

    
* **instance_type** (string)  

    
* **cloud_service_type** (string)  

    
* **cloud_service_group** (string)  

    
* **provider** (string)  

    
* **region_code** (string)  

    
* **ip_address** (string)  

    
* **project_id** (string)  

    
* **project_group_id** (string)  

    <br>

### CloudServiceReference
* **resource_id** (string)   `Required` 

    
* **external_link** (string)   `Required` 

    <br>

### CloudServiceRequest
* **cloud_service_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CloudServiceStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CloudServicesInfo
* **results** (CloudServiceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CollectionInfo
* **provider** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **collector_id** (string)   `Required` 

    
* **last_collected_at** (string)   `Required` 

    <br>

### CreateServiceRequest
* **cloud_service_type** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **cloud_service_group** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **account** (string)  

    
* **instance_type** (string)  

    
* **instance_size** (float)  

    
* **ip_addresses** (string)  `Repeated`   

    
* **metadata** (Struct)  

    
* **reference** (CloudServiceReference)  

    
* **tags** (Struct)  

    
* **region_code** (string)  

    
* **project_id** (string)  

    <br>

### GetCloudServiceRequest
* **cloud_service_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### PinCloudServiceDataRequest
* **cloud_service_id** (string)   `Required` 

    
* **keys** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### UpdateCloudServiceRequest
* **cloud_service_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **account** (string)  

    
* **instance_type** (string)  

    
* **instance_size** (float)  

    
* **ip_addresses** (string)  `Repeated`   

    
* **data** (Struct)  

    
* **metadata** (Struct)  

    
* **reference** (CloudServiceReference)  

    
* **tags** (Struct)  

    
* **region_code** (string)  

    
* **project_id** (string)  

    
* **release_project** (bool)  

    
* **release_region** (bool)  

    <br>
