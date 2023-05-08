---
title: "Cloud_service"
linkTitle: "Cloud_service"
weight: 3
bookFlatSection: true
---
# [Cloud_service](#Cloud_service)
desc: A CloudService is data of an `instance` of a `resource`. A CloudService follows the pre-created classification system of a CloudServiceType and indicates the property value of the `resource`.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Cloud_service


**CloudService Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudService#create) | [CreateServiceRequest](CloudService#createservicerequest) | [CloudServiceInfo](./CloudService#cloudserviceinfo) |
| [**update**](./CloudService#update) | [UpdateCloudServiceRequest](CloudService#updatecloudservicerequest) | [CloudServiceInfo](./CloudService#cloudserviceinfo) |
| [**delete**](./CloudService#delete) | [CloudServiceRequest](CloudService#cloudservicerequest) | [Empty](./CloudService#empty) |
| [**get**](./CloudService#get) | [GetCloudServiceRequest](CloudService#getcloudservicerequest) | [CloudServiceInfo](./CloudService#cloudserviceinfo) |
| [**list**](./CloudService#list) | [CloudServiceQuery](CloudService#cloudservicequery) | [CloudServicesInfo](./CloudService#cloudservicesinfo) |
| [**analyze**](./CloudService#analyze) | [CloudServiceAnalyzeQuery](CloudService#cloudserviceanalyzequery) | [Struct](./CloudService#struct) |
| [**stat**](./CloudService#stat) | [CloudServiceStatQuery](CloudService#cloudservicestatquery) | [Struct](./CloudService#struct) |



    
<br>

### create

> **POST** /inventory/v1/cloud-service/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /inventory/v1/cloud-service/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /inventory/v1/cloud-service/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/cloud-service/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/cloud-service/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### analyze

> **POST** /inventory/v1/cloud-service/analyze
>




 {{< tabs " analyze " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/cloud-service/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CloudServiceAnalyzeQuery
* **query** (AnalyzeQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceInfo
* **cloud_service_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (string)  `Required` 

    
* **account** (string)  `Required` 

    
* **instance_type** (string)  `Required` 

    
* **instance_size** (float)  `Required` 

    
* **cloud_service_type** (string)  `Required` 

    
* **cloud_service_group** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **data** (Struct)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **reference** (CloudServiceReference)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **tag_keys** (Struct)  `Required` 

    
* **collection_info** (CollectionInfo)  `Required` 

    
* **ip_addresses** (string)  `Required` 

    
* **region_code** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **deleted_at** (string)  `Required` 

    <br>

### CloudServiceQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **cloud_service_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **instance_type** (string)  `Required` 

  *is_required: false*

    
* **cloud_service_type** (string)  `Required` 

  *is_required: false*

    
* **cloud_service_group** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **region_code** (string)  `Required` 

  *is_required: false*

    
* **ip_address** (string)  `Required` 

  *is_required: false*

    
* **resource_group_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **project_group_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceReference
* **resource_id** (string)  `Required` 

    
* **external_link** (string)  `Required` 

    <br>

### CloudServiceRequest
* **cloud_service_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServicesInfo
* **results** (CloudServiceInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CollectionInfo
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

    
* **last_collected_at** (string)  `Required` 

    <br>

### CreateServiceRequest
* **cloud_service_type** (string)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: true*

    
* **cloud_service_group** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **instance_type** (string)  `Required` 

  *is_required: false*

    
* **instance_size** (float)  `Required` 

  *is_required: false*

    
* **ip_addresses** (string)  `Required` 

  *is_required: false*

    
* **data** (Struct)  `Required` 

  *is_required: true*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **reference** (CloudServiceReference)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **region_code** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetCloudServiceRequest
* **cloud_service_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PinCloudServiceDataRequest
* **cloud_service_id** (string)  `Required` 

  *is_required: true*

    
* **keys** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateCloudServiceRequest
* **cloud_service_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **instance_type** (string)  `Required` 

  *is_required: false*

    
* **instance_size** (float)  `Required` 

  *is_required: false*

    
* **ip_addresses** (string)  `Required` 

  *is_required: false*

    
* **data** (Struct)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **reference** (CloudServiceReference)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **region_code** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **release_project** (bool)  `Required` 

  *is_required: false*

    
* **release_region** (bool)  `Required` 

  *is_required: false*

    <br>
