<template>
  <div id="app" class="container mt-5">
    <h1 class="text-center mb-3">大黄瞎折腾之图片管理逻辑</h1>
    <div class="row mb-3">
      <div class="col">
        <input type="text" class="form-control" placeholder="搜索图片..." v-model="search" />
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

export default {
  name: 'App',
  components: {
    ImageUpload
  },
  data() {
    return {
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
    selectImage(image) {
      this.selectedImage = image;
    }
  }
}
</script>

<style>
/* 其他样式 */
.image-preview img {
  max-width: 100%;
  height: auto;
}
</style>
