// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: hotelService.proto

package com.example.demo;

public final class HotelServiceOuterClass {
  private HotelServiceOuterClass() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_com_example_demo_HotelRequest_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_com_example_demo_HotelRequest_fieldAccessorTable;
  static final com.google.protobuf.Descriptors.Descriptor
    internal_static_com_example_demo_HotelResponse_descriptor;
  static final 
    com.google.protobuf.GeneratedMessageV3.FieldAccessorTable
      internal_static_com_example_demo_HotelResponse_fieldAccessorTable;

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\022hotelService.proto\022\020com.example.demo\"-" +
      "\n\014HotelRequest\022\n\n\002id\030\001 \001(\005\022\021\n\thotelName\030" +
      "\002 \001(\t\"\"\n\rHotelResponse\022\021\n\thotelText\030\001 \001(" +
      "\t2[\n\014HotelService\022K\n\010getHotel\022\036.com.exam" +
      "ple.demo.HotelRequest\032\037.com.example.demo" +
      ".HotelResponseB\002P\001b\006proto3"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
        new com.google.protobuf.Descriptors.FileDescriptor.    InternalDescriptorAssigner() {
          public com.google.protobuf.ExtensionRegistry assignDescriptors(
              com.google.protobuf.Descriptors.FileDescriptor root) {
            descriptor = root;
            return null;
          }
        };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        }, assigner);
    internal_static_com_example_demo_HotelRequest_descriptor =
      getDescriptor().getMessageTypes().get(0);
    internal_static_com_example_demo_HotelRequest_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_com_example_demo_HotelRequest_descriptor,
        new java.lang.String[] { "Id", "HotelName", });
    internal_static_com_example_demo_HotelResponse_descriptor =
      getDescriptor().getMessageTypes().get(1);
    internal_static_com_example_demo_HotelResponse_fieldAccessorTable = new
      com.google.protobuf.GeneratedMessageV3.FieldAccessorTable(
        internal_static_com_example_demo_HotelResponse_descriptor,
        new java.lang.String[] { "HotelText", });
  }

  // @@protoc_insertion_point(outer_class_scope)
}
