<template>
    <div>
      <ul>
        <li v-for="image in images" :key="image">
          <img :src="image" @click="selectImage(image)" />
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ImageList',
    data() {
      return {
        images: [], // 图片数组，存储图片的URL
      };
    },
    methods: {
      selectImage(image) {
        // 选中图片的处理逻辑
        console.log("Image selected: ", image);
      },
      fetchImages() {
        // 获取图片列表的逻辑
        // 这里需要实现从后端API获取图片列表的逻辑
      }
    },
    mounted() {
      this.fetchImages();
    }
  }
  </script>
  