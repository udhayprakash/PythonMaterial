import boto3

session = boto3.Session()

print('Available AWS Resources:')
for resource in session.get_available_resources():
    print('\t', resource)

'''
Resources
    1. Services Resources - SQS, S3, EC2, ...
    2. Individual Resources - sqs.Queue, s3.Bucket, ...

'''

s3_reource = boto3.resource('s3')
print(vars(s3_reource))  # {'meta': ResourceMeta('s3', identifiers=[])}
print(dir(s3_reource))

['Bucket', 'BucketAcl', 'BucketCors', 'BucketLifecycle', 'BucketLifecycleConfiguration',
 'BucketLogging', 'BucketNotification', 'BucketPolicy', 'BucketRequestPayment',
 'BucketTagging', 'BucketVersioning', 'BucketWebsite', 'MultipartUpload',
 'MultipartUploadPart', 'Object', 'ObjectAcl', 'ObjectSummary', 'ObjectVersion',
   'buckets', 'create_bucket', 'get_available_subresources', 'meta']

s3_client = boto3.client('s3')
print(dir(s3_client))
['_PY_TO_OP_NAME', '_client_config', '_convert_to_request_dict', '_emit_api_params',
'_endpoint', '_exceptions', '_exceptions_factory', '_get_waiter_config',
'_load_exceptions', '_loader', '_make_api_call', '_make_request', '_register_handlers',
'_request_signer', '_response_parser', '_serializer', '_service_model',
'abort_multipart_upload', 'can_paginate', 'complete_multipart_upload',
'copy', 'copy_object', 'create_bucket', 'create_multipart_upload',
'delete_bucket', 'delete_bucket_analytics_configuration', 'delete_bucket_cors',
'delete_bucket_encryption', 'delete_bucket_intelligent_tiering_configuration',
'delete_bucket_inventory_configuration', 'delete_bucket_lifecycle',
'delete_bucket_metrics_configuration', 'delete_bucket_ownership_controls',
'delete_bucket_policy', 'delete_bucket_replication', 'delete_bucket_tagging',
'delete_bucket_website', 'delete_object', 'delete_object_tagging', 'delete_objects',
'delete_public_access_block', 'download_file', 'download_fileobj', 'exceptions',
'generate_presigned_post', 'generate_presigned_url', 'get_bucket_accelerate_configuration',
'get_bucket_acl', 'get_bucket_analytics_configuration', 'get_bucket_cors',
'get_bucket_encryption', 'get_bucket_intelligent_tiering_configuration',
'get_bucket_inventory_configuration', 'get_bucket_lifecycle',
'get_bucket_lifecycle_configuration', 'get_bucket_location', 'get_bucket_logging',
'get_bucket_metrics_configuration', 'get_bucket_notification',
'get_bucket_notification_configuration', 'get_bucket_ownership_controls',
'get_bucket_policy', 'get_bucket_policy_status', 'get_bucket_replication',
'get_bucket_request_payment', 'get_bucket_tagging', 'get_bucket_versioning',
'get_bucket_website', 'get_object', 'get_object_acl', 'get_object_legal_hold',
'get_object_lock_configuration', 'get_object_retention', 'get_object_tagging',
'get_object_torrent', 'get_paginator', 'get_public_access_block', 'get_waiter',
 'head_bucket', 'head_object', 'list_bucket_analytics_configurations',
'list_bucket_intelligent_tiering_configurations', 'list_bucket_inventory_configurations',
'list_bucket_metrics_configurations', 'list_buckets', 'list_multipart_uploads',
'list_object_versions', 'list_objects', 'list_objects_v2', 'list_parts', 'meta',
'put_bucket_accelerate_configuration', 'put_bucket_acl', 'put_bucket_analytics_configuration',
'put_bucket_cors', 'put_bucket_encryption', 'put_bucket_intelligent_tiering_configuration',
'put_bucket_inventory_configuration', 'put_bucket_lifecycle', 'put_bucket_lifecycle_configuration',
'put_bucket_logging', 'put_bucket_metrics_configuration', 'put_bucket_notification',
'put_bucket_notification_configuration', 'put_bucket_ownership_controls',
'put_bucket_policy', 'put_bucket_replication', 'put_bucket_request_payment',
'put_bucket_tagging', 'put_bucket_versioning', 'put_bucket_website', 'put_object',
 'put_object_acl', 'put_object_legal_hold', 'put_object_lock_configuration',
 'put_object_retention', 'put_object_tagging', 'put_public_access_block', 'restore_object',
  'select_object_content', 'upload_file', 'upload_fileobj', 'upload_part', 'upload_part_copy',
  'waiter_names', 'write_get_object_response']
