<template>
  <div id="app" class="container mt-5">
    <h1 class="text-center mb-3">大黄瞎折腾之图片管理逻辑</h1>
    <div class="row mb-3">
      <div class="col">
        <input type="text" class="form-control" placeholder="搜索图片..." v-model="search" />
        <button class="btn btn-primary mr-2" @click="showUpload = true">上传</button>
        <button class="btn btn-danger" @click="deleteSelectedImages" :disabled="!selectedImages.length">删除选中</button>
      </div>
    </div>
    <div class="row" v-if="showUpload">
      <div class="col-12">
        <ImageUpload @image-uploaded="handleImageUploaded" />
      </div>
    </div>
    <div class="row">
      <div class="col-md-4">
        <div class="card" style="max-height: 500px; overflow-y: auto;">
          <div class="card-header">
            图片列表
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item" v-for="image in filteredImages" :key="image.name" @click="selectImage(image)">
              {{ image.name }}
            </li>
          </ul>
        </div>
      </div>
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">
            图片预览
          </div>
          <div class="card-body">
            <div v-if="selectedImage" class="image-preview">
              <img :src="selectedImage.url" class="img-fluid" alt="Selected Image">
            </div>
            <!-- 如果没有选中的图片，则显示上传组件 -->
            <ImageUpload v-else />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ImageUpload from './components/ImageUpload.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    ImageUpload
  },
  data() {
    return {
      showUpload: true,  // 控制是否显示上传组件
      selectedImages: [],  // 用于存储选中的图片
      search: '',
      images: [
        { name: '截图jietu01', url: '/img/123.png' },
        { name: 'Image2', url: '/img/312.jpg' },
        // 更多图片
      ],
      selectedImage: null
    };
  },
  computed: {
    filteredImages() {
      return this.images.filter(image => {
        return image.name.toLowerCase().includes(this.search.toLowerCase());
      });
    }
  },
  methods: {
    handleImageUploaded(uploadedImage) {
      this.images.push(uploadedImage); // 假设uploadedImage是包含name和url的对象
      this.showUpload = false;  // 上传后隐藏上传组件
    },
    deleteSelectedImages() {
      if (!this.selectedImages.length) {
        alert('请选择要删除的图片');
        return;
      }

      const selectedNames = this.selectedImages.map(image => image.name);
      axios.post('/delete-image', { names: selectedNames })
        .then(() => {
          this.images = this.images.filter(image => !selectedNames.includes(image.name));
          this.selectedImages = [];
        })
        .catch(error => {
          console.error('删除失败:', error);
        });
    },
    selectImage(image) {
      this.selectedImage = image; // 确保你有一个data属性叫selectedImage
    },
    // ...可能的其他方法
  },
  // ...其他选项
}
</script>

<style>
/* 其他样式 */
.image-preview img {
  max-width: 100%;
  height: auto;
}
</style>
