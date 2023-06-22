# `Byte` - `FDI(Food of Daegu information)`

해커그라운드 해커톤에 참여하는 `Byte` 팀의 `FDI(Food of Deagu Information)`입니다.

## 참고 문서

> 아래 두 링크는 해커톤에서 앱을 개발하면서 참고할 만한 문서들입니다. 이 문서들에서 언급한 서비스 이외에도 더 많은 서비스들이 PaaS, SaaS, 서버리스 형태로 제공되니 참고하세요.

- [순한맛](./REFERENCES_BASIC.md)
- [매운맛](./REFERENCES_ADVANCED.md)

## 제품/서비스 소개

<!-- 아래 링크는 지우지 마세요 -->
[제품/서비스 소개 보기](TOPIC.md)
<!-- 위 링크는 지우지 마세요 -->

## 오픈 소스 라이센스

<!-- 아래 링크는 지우지 마세요 -->
[오픈소스 라이센스 보기](./LICENSE)
<!-- 위 링크는 지우지 마세요 -->

## 설치 방법
- [github](https://github.com) 에서 회원가입한다.
- [azure](azure.microsoft.com)구독하기
- [visual studio](http://visualstudio.microsoft.com)가서 깔기


### 사전 준비 사항

- [Microsoft Azure](https://portal.azure.com)
- [github](https://github.com) : github account
- [azure](azure.microsoft.com) : azure free account
- [visual studio](http://visualstudio.microsoft.com) : visual studio code

## 시작하기
1. 포크뜨기

[hackersground-kr/Byte](https://github.com/hackersground-kr/Byte)에 접속한다.

<img width="592" alt="Fork2" src="https://github.com/hackersground-kr/Byte/assets/106953846/f36247b6-1678-4e90-9c8f-01b2b596f1ff">

사진에 보이는 fork를 누르고 create fork 버튼을 눌러준다.


2. 리소스 그룹 만들기

[Microsoft Azure](https://portal.azure.com)에 로그인한다.

좌측 상단의 줄 3개 모양 버튼을 누르면 나오는 리소스 그룹 버튼을 클릭하고 만들기를 누른다.

누르면 나오는 화면에서 리소스 그룹 옆 칸에 rg-hg-원하는이름(*단, 중복이 되지 않도록 유니크한 이름으로)을 적는다.

리소스 영역은 (Asia Pacific) Korea Central을 선택한다.

하단에 있는 검토+만들기를 클릭하고 만들기 버튼을 누른다.


3. 리소스 만들기

좌측 상단에 줄 세개짜리를 누르고 '모든 서비스'를 누른다.

'리소스 그룹'을 클릭한다.

![image](https://github.com/hackersground-kr/Byte/assets/106953846/cf4b9786-92f7-4a6f-ba39-925a4d5b5694)

2번에서 만들었던 '리소스 그룹'을 클릭한다.(①)

우측 상단에 '+만들기'를 누른다.(②)

웹앱을 검색하거나 스크롤을 내려서 찾아 클릭하고 만들기를 누른다.

들어가자마자 " 기본 | 배포 | 네트워킹 | 모니터링 | 태그 | 검토+만들기 " 로 카테고리가 나눠진 화면이 보일 것이다. 각각에 대한 설명을 상세하게 적겠다.

기본 카테고리에서 할 일)

- 구독 옆에는 Hackers Ground 설정한 후, 구독에 연결된 리소스 그룹에 rg-hg-byte를 입력한다.
- 웹앱 이름은 중복되지 않는 원하는 이름으로 선택한다.
- 게시는 코드를 선택한다.
- 런타임 스택에 Python 3.8을 선택한다.
- 운영체제 Linux를 선택한다.
- 지역에는 Korea Central을 선택한다.
- Linux plan은 (신규)ASP-rghgByte-8a60 선택
- 가격책정에는 기본B1(100총 ACU, 1.75GB 메모리, 1vCPU) 선택
- 영역중복은 건드리지 않고 넘어간다.

왼쪽 하단에 "다음:배포" 버튼을 클릭한다.
  
배포에서 할 일)

-Github Action 설정 – 지속적인 배포 사용을 선택한다.

-Github 계정 권한부여를 누르고 뜨는 화면에 password를 입력한다.

- 조직은 hackersground-kr 선택

- 리포지토리는 Byte 선택
- 분기는 main 선택

*네트워킹, 모니터링, 태그는 패스한다.

검토+만들기)

-설정했던 값이 맞는지 확인한 후 만들기를 누른다. 

-배포 진행 중에서 배포가 완료됨이 뜰 때 까지 기다린다.

-배포가 완료됨이 뜨면 리소스로 이동을 누른다.

![image](https://github.com/hackersground-kr/Byte/assets/106953846/d3ada655-be08-48c6-825c-162fd179712b)

-이동을 누르면 나타나는 화면에 오른쪽 5번째 줄에 github프로젝트 옆에 있는 링크를 누른다.

그다음 Actions에 들어간다.

![image](https://github.com/hackersground-kr/Byte/assets/106953846/8011589f-97ca-45b2-9e22-dd321931db1c)


들어가면 본인이 설정한 웹앱 이름으로 리소스가 만들어진 것을 볼 수 있다. ( 빨간색 네모 )

![image](https://github.com/hackersground-kr/Byte/assets/106953846/066a5db8-5813-42e2-8220-d9dbab169131)

- 좌측의 노란 버튼이 초록색으로 된 것을 확인하고 리소스 이름을 클릭하여 다음 창으로 가 deploy 밑의 링크를 타고 들어간다.

![image](https://github.com/hackersground-kr/Byte/assets/106953846/8f4713fc-7314-44b8-a4f0-2d0fc9cd02c4)

그 링크를 들어가서 welcome to azure 뜨면 배포가 성공된 것이다. 



