---
title: "Asset"
linkTitle: "Asset"
weight: 3
bookFlatSection: true
---
# [Asset](#Asset)
A Asset is data of an `instance` of a `resource`. A Asset follows the pre-created classification system of a AssetType and indicates the property value of the `resource`.


>  **Package : spaceone.api.inventory_v2.v1**

<br>
<br>

## Asset





**Asset Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Asset#create) | [AssetCreateRequest](Asset#assetcreaterequest) | [AssetInfo](Asset#assetinfo) |
| [**update**](./Asset#update) | [UpdateAssetRequest](Asset#updateassetrequest) | [AssetInfo](Asset#assetinfo) |
| [**delete**](./Asset#delete) | [AssetRequest](Asset#assetrequest) | [Empty](Asset#empty) |
| [**get**](./Asset#get) | [AssetRequest](Asset#assetrequest) | [AssetInfo](Asset#assetinfo) |
| [**list**](./Asset#list) | [AssetQuery](Asset#assetquery) | [AssetsInfo](Asset#assetsinfo) |
| [**export**](./Asset#export) | [AssetExportRequest](Asset#assetexportrequest) | [Struct](Asset#struct) |
| [**history**](./Asset#history) | [AssetHistoryQuery](Asset#assethistoryquery) | [AssetHistoriesInfo](Asset#assethistoriesinfo) |
| [**analyze**](./Asset#analyze) | [AssetAnalyzeQuery](Asset#assetanalyzequery) | [Struct](Asset#struct) |
| [**stat**](./Asset#stat) | [AssetStatQuery](Asset#assetstatquery) | [Struct](Asset#struct) |



    
<br>

### create

Creates a new Asset. A Asset instance is created based on data including the `resource`'s attribute values. When creating, the classification information defined by AssetType is also needed. The created Asset has collection information which is the collection history for the `resource` by plugin.



> **POST** /inventory-v2/v1/asset/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[AssetCreateRequest](./Asset#assetcreaterequest)

* **asset_type_id** (string)   `Required` 


* **provider** (string)   `Required` 


* **data** (Struct)   `Required` 


* **name** (string)  


* **account** (string)  


* **ip_addresses** (string)  `Repeated`   


* **metadata** (Struct)  


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

[AssetInfo](#ASSETINFO)
* **asset_id** (string)   `Required` 

  This id value is unique at each domain.

* **name** (string)   `Required` 

  Name of cloud resource from CSP like AWS, Azure, GCP

* **state** (string)   `Required` 

  State of cloud resource

* **ip_addresses** (string)  `Repeated`   `Required` 

  IP addresses of cloud resource having public IP

* **account** (string)   `Required` 

  Account ID of cloud resource

* **asset_type_id** (string)   `Required` 

  Classification of cloud resource

* **provider** (string)   `Required` 

  Cloud Service provider like AWS, Azure, GCP

* **data** (Struct)   `Required` 

  Original data from CSP

* **tags** (Struct)   `Required` 

  Tags from CSP

* **region_id** (string)   `Required` 

  Collection information

* **domain_id** (string)   `Required` 

  Domain Id

* **workspace_id** (string)   `Required` 

  Workspace Id

* **project_id** (string)   `Required` 

  Project Id

* **collector_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

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
       "custom": {
             "b" : "c"
       },
       "aws" : {
             "env": "dev"
       }
   },
   "collection_info": {
       "service_account_id": "sa-abcd1234",
       "secret_id": "secret-abcd1234",
       "collector_id": "collector-abcd1234",
       "last_collected_at": "2022-06-22T06:38:48.989Z"
   },
   "ip_addresses": [],
   "region_code": "ap-northeast-1",
   "workspace_id": "workspace-58010aa2e451",
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

Updates a specific Asset. You can make changes in Asset settings, except for the classification system of Asset and the information about the `resource` attribute value.



> **POST** /inventory-v2/v1/asset/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateAssetRequest](./Asset#updateassetrequest)

* **cloud_service_id** (string)   `Required` 


* **name** (string)  


* **account** (string)  


* **instance_type** (string)  


* **instance_size** (float)  


* **ip_addresses** (string)  `Repeated`   


* **data** (Struct)  


* **metadata** (Struct)  


* **tags** (Struct)  


* **region_code** (string)  


* **project_id** (string)  





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

[AssetInfo](#ASSETINFO)
* **asset_id** (string)   `Required` 

  This id value is unique at each domain.

* **name** (string)   `Required` 

  Name of cloud resource from CSP like AWS, Azure, GCP

* **state** (string)   `Required` 

  State of cloud resource

* **ip_addresses** (string)  `Repeated`   `Required` 

  IP addresses of cloud resource having public IP

* **account** (string)   `Required` 

  Account ID of cloud resource

* **asset_type_id** (string)   `Required` 

  Classification of cloud resource

* **provider** (string)   `Required` 

  Cloud Service provider like AWS, Azure, GCP

* **data** (Struct)   `Required` 

  Original data from CSP

* **tags** (Struct)   `Required` 

  Tags from CSP

* **region_id** (string)   `Required` 

  Collection information

* **domain_id** (string)   `Required` 

  Domain Id

* **workspace_id** (string)   `Required` 

  Workspace Id

* **project_id** (string)   `Required` 

  Project Id

* **collector_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

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
       "custom": {
             "b" : "c"
       },
       "aws" : {
             "env": "dev"
       }
   },
   "collection_info": {
       "service_account_id": "sa-abcd1234",
       "secret_id": "secret-abcd1234",
       "collector_id": "collector-abcd1234",
       "last_collected_at": "2022-06-22T06:38:48.989Z"
   },
   "ip_addresses": [],
   "region_code": "ap-northeast-1",
   "workspace_id": "workspace-58010aa2e451",
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

Deletes a specific Asset. You must specify the `cloud_service_id` of the Asset to delete.



> **POST** /inventory-v2/v1/asset/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[AssetRequest](./Asset#assetrequest)

* **asset_id** (string)   `Required` 





{{< highlight json >}}
{
   "asset_id": "asset-fea2b0d32141"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Asset. Prints detailed information about the Asset, including its state, classification information, and attribute values.



> **POST** /inventory-v2/v1/asset/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[AssetRequest](./Asset#assetrequest)

* **asset_id** (string)   `Required` 





{{< highlight json >}}
{
   "asset_id": "asset-fea2b0d32141"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AssetInfo](#ASSETINFO)
* **asset_id** (string)   `Required` 

  This id value is unique at each domain.

* **name** (string)   `Required` 

  Name of cloud resource from CSP like AWS, Azure, GCP

* **state** (string)   `Required` 

  State of cloud resource

* **ip_addresses** (string)  `Repeated`   `Required` 

  IP addresses of cloud resource having public IP

* **account** (string)   `Required` 

  Account ID of cloud resource

* **asset_type_id** (string)   `Required` 

  Classification of cloud resource

* **provider** (string)   `Required` 

  Cloud Service provider like AWS, Azure, GCP

* **data** (Struct)   `Required` 

  Original data from CSP

* **tags** (Struct)   `Required` 

  Tags from CSP

* **region_id** (string)   `Required` 

  Collection information

* **domain_id** (string)   `Required` 

  Domain Id

* **workspace_id** (string)   `Required` 

  Workspace Id

* **project_id** (string)   `Required` 

  Project Id

* **collector_id** (string)   `Required` 

* **service_account_id** (string)   `Required` 

* **secret_id** (string)   `Required` 

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
       "custom": {
             "b" : "c"
       },
       "aws" : {
             "env": "dev"
       }
   },
   "collection_info": {
       "service_account_id": "sa-abcd1234",
       "secret_id": "secret-abcd1234",
       "collector_id": "collector-abcd1234",
       "last_collected_at": "2022-06-22T06:38:48.989Z"
   },
   "ip_addresses": [],
   "region_code": "ap-northeast-1",
   "workspace_id": "workspace-58010aa2e451",
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

Gets a list of all Assets. You can use a query to get a filtered list of Assets.



> **POST** /inventory-v2/v1/asset/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[AssetQuery](./Asset#assetquery)

* **query** (Query)  


* **asset_id** (string)  


* **name** (string)  


* **state** (string)  


* **ip_address** (string)  


* **account** (string)  


* **asset_type_id** (string)  


* **provider** (string)  


* **region_id** (string)  


* **workspace_id** (string)  


* **project_id** (string)  


* **project_group_id** (string)  





{{< highlight json >}}
{
   "query": {
       "filter": [
           {
               "key": "asset_type_id",
               "value": "Key",
               "operator": "eq"
           }
       ]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[AssetsInfo](#ASSETSINFO)
* **results** (AssetInfo)  `Repeated`   `Required` 

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
            "service_account_id": "sa-abcd1234",
            "secret_id": "secret-abcd1234",
            "collector_id": "collector-abcd1234",
            "last_collected_at": "2022-06-22T06:38:48.989Z"
       },
       "ip_addresses": [
           "1.1.1.1",
           "2.2.2.2"
       ],
       "region_code": "ap-northeast-1",
       "workspace_id": "workspace-58010aa2e451",
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





> **POST** /inventory-v2/v1/asset/export
>






    
<br>

### history





> **POST** /inventory-v2/v1/asset/history
>





 {{< tabs " history " >}}

 {{< tab "Request Example" >}}



[AssetHistoryQuery](./Asset#assethistoryquery)

* **asset_id** (string)   `Required` 


* **query** (Query)  


* **history_id** (string)  


* **action** (RecordAction)  


* **updated_by** (string)  


* **collector_id** (string)  


* **job_id** (string)  


* **user_id** (string)  





{{< highlight json >}}
{
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### analyze





> **POST** /inventory-v2/v1/asset/analyze
>






    
<br>

### stat





> **POST** /inventory-v2/v1/asset/stat
>






    


<br>
<br>

## Message



### AssetAnalyzeQuery
* **query** (AnalyzeQuery)   `Required` 

    <br>

### AssetCreateRequest
* **asset_type_id** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **data** (Struct)   `Required` 

    
* **name** (string)  

    
* **account** (string)  

    
* **ip_addresses** (string)  `Repeated`   

    
* **metadata** (Struct)  

    
* **tags** (Struct)  

    
* **region_code** (string)  

    
* **project_id** (string)  

    <br>

### AssetExportRequest
* **options** (ExportOption)  `Repeated`    `Required` 

    
* **file_format** (FileFormat)  

    
* **file_name** (string)  

    
* **timezone** (string)  

    <br>

### AssetHistoriesInfo
* **results** (AssetHistoryInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### AssetHistoryInfo
* **history_id** (string)   `Required` 

    
* **asset_id** (string)   `Required` 

    
* **action** (Action)   `Required` 

    
* **diff** (Struct)  `Repeated`    `Required` 

    
* **diff_count** (int32)   `Required` 

    
* **updated_by** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **collector_id** (string)   `Required` 

    
* **job_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### AssetHistoryQuery
* **asset_id** (string)   `Required` 

    
* **query** (Query)  

    
* **history_id** (string)  

    
* **action** (RecordAction)  

    
* **updated_by** (string)  

    
* **collector_id** (string)  

    
* **job_id** (string)  

    
* **user_id** (string)  

    <br>

### AssetInfo
* **asset_id** (string)   `Required` 

  *This id value is unique at each domain.*

    
* **name** (string)   `Required` 

  *Name of cloud resource from CSP like AWS, Azure, GCP*

    
* **state** (string)   `Required` 

  *State of cloud resource*

    
* **ip_addresses** (string)  `Repeated`    `Required` 

  *IP addresses of cloud resource having public IP*

    
* **account** (string)   `Required` 

  *Account ID of cloud resource*

    
* **asset_type_id** (string)   `Required` 

  *Classification of cloud resource*

    
* **provider** (string)   `Required` 

  *Cloud Service provider like AWS, Azure, GCP*

    
* **data** (Struct)   `Required` 

  *Original data from CSP*

    
* **tags** (Struct)   `Required` 

  *Tags from CSP*

    
* **region_id** (string)   `Required` 

  *Collection information*

    
* **domain_id** (string)   `Required` 

  *Domain Id*

    
* **workspace_id** (string)   `Required` 

  *Workspace Id*

    
* **project_id** (string)   `Required` 

  *Project Id*

    
* **collector_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    <br>

### AssetQuery
* **query** (Query)  

    
* **asset_id** (string)  

    
* **name** (string)  

    
* **state** (string)  

    
* **ip_address** (string)  

    
* **account** (string)  

    
* **asset_type_id** (string)  

    
* **provider** (string)  

    
* **region_id** (string)  

    
* **workspace_id** (string)  

    
* **project_id** (string)  

    
* **project_group_id** (string)  

    <br>

### AssetRequest
* **asset_id** (string)   `Required` 

    <br>

### AssetStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### AssetsInfo
* **results** (AssetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateAssetRequest
* **cloud_service_id** (string)   `Required` 

    
* **name** (string)  

    
* **account** (string)  

    
* **instance_type** (string)  

    
* **instance_size** (float)  

    
* **ip_addresses** (string)  `Repeated`   

    
* **data** (Struct)  

    
* **metadata** (Struct)  

    
* **tags** (Struct)  

    
* **region_code** (string)  

    
* **project_id** (string)  

    <br>
