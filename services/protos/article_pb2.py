# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: article.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'article.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rarticle.proto\x1a\x1bgoogle/protobuf/empty.proto\"I\n\x07\x41rticle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x04 \x01(\t\"5\n\x12\x41rticleListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\"1\n\x13\x41rticleListResponse\x12\x1a\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x08.Article\"\"\n\x14\x41rticleDetailRequest\x12\n\n\x02pk\x18\x01 \x01(\x05\"2\n\x15\x41rticleDetailResponse\x12\x19\n\x07\x61rticle\x18\x01 \x01(\x0b\x32\x08.Article\"J\n\x14\x43reateArticleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\t\"2\n\x15\x43reateArticleResponse\x12\x19\n\x07\x61rticle\x18\x01 \x01(\x0b\x32\x08.Article\"V\n\x14UpdateArticleRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x04 \x01(\t\"\"\n\x14\x44\x65leteArticleRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\xca\x02\n\x0e\x41rticleService\x12\x38\n\x0b\x41rticleList\x12\x13.ArticleListRequest\x1a\x14.ArticleListResponse\x12>\n\rArticleDetail\x12\x15.ArticleDetailRequest\x1a\x16.ArticleDetailResponse\x12>\n\rCreateArticle\x12\x15.CreateArticleRequest\x1a\x16.CreateArticleResponse\x12>\n\rUpdateArticle\x12\x15.UpdateArticleRequest\x1a\x16.google.protobuf.Empty\x12>\n\rDeleteArticle\x12\x15.DeleteArticleRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'article_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ARTICLE']._serialized_start=46
  _globals['_ARTICLE']._serialized_end=119
  _globals['_ARTICLELISTREQUEST']._serialized_start=121
  _globals['_ARTICLELISTREQUEST']._serialized_end=174
  _globals['_ARTICLELISTRESPONSE']._serialized_start=176
  _globals['_ARTICLELISTRESPONSE']._serialized_end=225
  _globals['_ARTICLEDETAILREQUEST']._serialized_start=227
  _globals['_ARTICLEDETAILREQUEST']._serialized_end=261
  _globals['_ARTICLEDETAILRESPONSE']._serialized_start=263
  _globals['_ARTICLEDETAILRESPONSE']._serialized_end=313
  _globals['_CREATEARTICLEREQUEST']._serialized_start=315
  _globals['_CREATEARTICLEREQUEST']._serialized_end=389
  _globals['_CREATEARTICLERESPONSE']._serialized_start=391
  _globals['_CREATEARTICLERESPONSE']._serialized_end=441
  _globals['_UPDATEARTICLEREQUEST']._serialized_start=443
  _globals['_UPDATEARTICLEREQUEST']._serialized_end=529
  _globals['_DELETEARTICLEREQUEST']._serialized_start=531
  _globals['_DELETEARTICLEREQUEST']._serialized_end=565
  _globals['_ARTICLESERVICE']._serialized_start=568
  _globals['_ARTICLESERVICE']._serialized_end=898
# @@protoc_insertion_point(module_scope)
