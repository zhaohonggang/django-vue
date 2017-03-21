<template>
    <div class="login-wrap">
        <div class="ms-title">Backend Management</div>
        <div class="ms-login">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="username"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="password" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">Login</el-button>
                </div>
                <p style="font-size:12px;line-height:30px;color:#999;">Tips : Please login</p>
            </el-form>
        </div>
    </div>
</template>

<script>
    //import axios from 'axios';
    export default {
        data (){
            return {
                ruleForm: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        { required: true, message: 'Please input Username', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: 'Please input Password', trigger: 'blur' }
                    ]
                }
            }
        },
        mounted () {
            this.requestUser();
            //console.log('hook-example activated!');
            //document.title = 'Manage2';
            //const self = this;
            //this.$router.push('/readme');
        },
        methods: {
            requestUser:function() {
                const self = this;
                //document.title = 'Manage2';
                //console.log(Cookies.get('token'));
                let username = localStorage.getItem('ms_username');
                if (username)
                {
                    axios.get(GCGAPIHOST+'/api/request_user/', {
                        headers:{ 
                        Authorization: 'Token ' + Cookies.get('token')
                    }
                    }).then(response => {
                            //console.log(response.body.user);
                            localStorage.setItem('ms_username',response.data.user);
                            //console.log('call api succeed!');
                            // console.log(response.data.user);
                            this.$router.push('/begin');
                        }).catch( response => {
                            //this.currentView = 'login-page'
                            // this.$router.push('/readme');
                            //console.log('call api failed!');
                            console.log(response);
                        })
                }
                },
            submitForm(formName) {
                const self = this;
                self.$refs[formName].validate((valid) => {
                    if (valid) {
                           axios.post(GCGAPIHOST+'/api/login/',{
                                username: this.ruleForm.username,
                                password: this.ruleForm.password
                            },).then(response => {
                                if(response.data.url)
                                {
                                    location.href = response.data.url;
                                }
                                else if(response.data.token){
                                    Cookies.set('token', response.data.token, { expires: 365});
                                // this.loginSuccess()
                                    localStorage.setItem('ms_username',self.ruleForm.username);
                                    self.$router.push('/begin');
                                }
                                else{
                                    console.log('error submit!!');
                                    return false;
                                
                                }
                                }).catch(function (response) {
                           // this.msg = '帐号或密码错误';
                         console.log('error submit!!');
                         return false;
                   });
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .login-wrap{
        position: relative;
        width:100%;
        height:100%;
    }
    .ms-title{
        position: absolute;
        top:50%;
        width:100%;
        margin-top: -230px;
        text-align: center;
        font-size:30px;
        color: #fff;

    }
    .ms-login{
        position: absolute;
        left:50%;
        top:50%;
        width:300px;
        height:160px;
        margin:-150px 0 0 -190px;
        padding:40px;
        border-radius: 5px;
        background: #fff;
    }
    .login-btn{
        text-align: center;
    }
    .login-btn button{
        width:100%;
        height:36px;
    }
</style>