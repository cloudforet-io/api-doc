---
title: "CloudServiceType"
linkTitle: "CloudServiceType"
weight: 3
bookFlatSection: true
---
# [CloudServiceType](#CloudServiceType)
A CloudServiceType is a classification with hierarchical information of `CloudService`. A CloudServiceType provides information about which `group` a specific `Resource` belongs to and which `Services` are in it.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## CloudServiceType





**CloudServiceType Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudServiceType#create) | [CreateCloudServiceTypeRequest](CloudServiceType#createcloudservicetyperequest) | [CloudServiceTypeInfo](CloudServiceType#cloudservicetypeinfo) |
| [**update**](./CloudServiceType#update) | [UpdateCloudServiceTypeRequest](CloudServiceType#updatecloudservicetyperequest) | [CloudServiceTypeInfo](CloudServiceType#cloudservicetypeinfo) |
| [**delete**](./CloudServiceType#delete) | [CloudServiceTypeRequest](CloudServiceType#cloudservicetyperequest) | [Empty](CloudServiceType#empty) |
| [**get**](./CloudServiceType#get) | [CloudServiceTypeRequest](CloudServiceType#cloudservicetyperequest) | [CloudServiceTypeInfo](CloudServiceType#cloudservicetypeinfo) |
| [**list**](./CloudServiceType#list) | [CloudServiceTypeQuery](CloudServiceType#cloudservicetypequery) | [CloudServiceTypesInfo](CloudServiceType#cloudservicetypesinfo) |
| [**stat**](./CloudServiceType#stat) | [CloudServiceTypeStatQuery](CloudServiceType#cloudservicetypestatquery) | [Struct](CloudServiceType#struct) |



    
<br>

### create

Creates a new CloudServiceType. You must specify the `name`, `provider`, and `group` parameters to create a CloudServiceType. One or several CloudServiceTypes exist in a specific `group`, and each CloudServiceType is identified by the `name` parameter.



> **POST** /inventory/v1/cloud-service-type/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCloudServiceTypeRequest](./CloudServiceType#createcloudservicetyperequest)

* **name** (string)   `Required` 


* **provider** (string)   `Required` 


* **group** (string)   `Required` 


* **service_code** (string)  


* **is_primary** (bool)  


* **is_major** (bool)  


* **resource_type** (string)  


* **metadata** (Struct)  


* **labels** (ListValue)  


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceTypeInfo](#CLOUDSERVICETYPEINFO)
* **cloud_service_type_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **group** (string)   `Required` 

* **cloud_service_type_key** (string)   `Required` 

* **service_code** (string)   `Required` 

* **is_primary** (bool)   `Required` 

* **is_major** (bool)   `Required` 

* **resource_type** (string)   `Required` 

* **metadata** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
   "workspace_id": "workspace-abcde12345",
   "created_at": "2022-06-22T01:38:16.301Z",
   "updated_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific CloudServiceType. You can make changes in CloudServiceType settings, except for `name`, `provider` and `group`. In particular, you can set the CloudServiceType's priority in a `group`.



> **POST** /inventory/v1/cloud-service-type/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateCloudServiceTypeRequest](./CloudServiceType#updatecloudservicetyperequest)

* **cloud_service_type_id** (string)   `Required` 


* **service_code** (string)  


* **is_primary** (bool)  


* **is_major** (bool)  


* **resource_type** (string)  


* **metadata** (Struct)  


* **labels** (ListValue)  


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceTypeInfo](#CLOUDSERVICETYPEINFO)
* **cloud_service_type_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **group** (string)   `Required` 

* **cloud_service_type_key** (string)   `Required` 

* **service_code** (string)   `Required` 

* **is_primary** (bool)   `Required` 

* **is_major** (bool)   `Required` 

* **resource_type** (string)   `Required` 

* **metadata** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
   "workspace_id": "workspace-abcde12345",
   "created_at": "2022-06-22T01:38:16.301Z",
   "updated_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific CloudServiceType. You must specify the `cloud_service_type_id` of the CloudServiceType to delete.



> **POST** /inventory/v1/cloud-service-type/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CloudServiceTypeRequest](./CloudServiceType#cloudservicetyperequest)

* **cloud_service_type_id** (string)   `Required` 





{{< highlight json >}}
{
   "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific CloudServiceType. Prints detailed information about the CloudServiceType.



> **POST** /inventory/v1/cloud-service-type/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[CloudServiceTypeRequest](./CloudServiceType#cloudservicetyperequest)

* **cloud_service_type_id** (string)   `Required` 





{{< highlight json >}}
{
   "cloud_service_type_id": "cloud-svc-type-27dd73ac89f8"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceTypeInfo](#CLOUDSERVICETYPEINFO)
* **cloud_service_type_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **group** (string)   `Required` 

* **cloud_service_type_key** (string)   `Required` 

* **service_code** (string)   `Required` 

* **is_primary** (bool)   `Required` 

* **is_major** (bool)   `Required` 

* **resource_type** (string)   `Required` 

* **metadata** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
   "workspace_id": "workspace-abcde12345",
   "created_at": "2022-06-22T01:38:16.301Z",
   "updated_at": "2022-06-22T01:38:16.301Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all CloudServiceTypes. You can use a query to get a filtered list of CloudServiceTypes.



> **POST** /inventory/v1/cloud-service-type/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CloudServiceTypeQuery](./CloudServiceType#cloudservicetypequery)

* **query** (Query)  


* **cloud_service_type_id** (string)  


* **name** (string)  


* **provider** (string)  


* **group** (string)  


* **cloud_service_type_key** (string)  


* **service_code** (string)  


* **is_primary** (bool)  


* **is_major** (bool)  


* **resource_type** (string)  


* **workspace_id** (string)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CloudServiceTypesInfo](#CLOUDSERVICETYPESINFO)
* **results** (CloudServiceTypeInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
           "workspace_id": "workspace-abcde12345",
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
           "workspace_id": "workspace-abcde12345",
           "created_at": "2021-06-03T02:29:53.052Z",
           "updated_at": "2022-06-22T00:05:41.252Z"
       }
   ],
   "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/cloud-service-type/stat
>






    


<br>
<br>

## Message



### CloudServiceTypeInfo
* **cloud_service_type_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **group** (string)   `Required` 

    
* **cloud_service_type_key** (string)   `Required` 

    
* **service_code** (string)   `Required` 

    
* **is_primary** (bool)   `Required` 

    
* **is_major** (bool)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### CloudServiceTypeQuery
* **query** (Query)  

    
* **cloud_service_type_id** (string)  

    
* **name** (string)  

    
* **provider** (string)  

    
* **group** (string)  

    
* **cloud_service_type_key** (string)  

    
* **service_code** (string)  

    
* **is_primary** (bool)  

    
* **is_major** (bool)  

    
* **resource_type** (string)  

    
* **workspace_id** (string)  

    <br>

### CloudServiceTypeRequest
* **cloud_service_type_id** (string)   `Required` 

    <br>

### CloudServiceTypeStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CloudServiceTypesInfo
* **results** (CloudServiceTypeInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCloudServiceTypeRequest
* **name** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **group** (string)   `Required` 

    
* **service_code** (string)  

    
* **is_primary** (bool)  

    
* **is_major** (bool)  

    
* **resource_type** (string)  

    
* **metadata** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### UpdateCloudServiceTypeRequest
* **cloud_service_type_id** (string)   `Required` 

    
* **service_code** (string)  

    
* **is_primary** (bool)  

    
* **is_major** (bool)  

    
* **resource_type** (string)  

    
* **metadata** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>
