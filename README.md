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
https://github.com/ 에서 회원가입한다.


### 사전 준비 사항

- [Microsoft Azure](https://portal.azure.com)
- github account
- azure free account
- visual studio code

## 시작하기
[Microsoft Azure](https://portal.azure.com)에 접속한다.

fork를 뜬다.

좌측 상단에 줄 세개짜리를 누르고 '모든 서비스'를 누른다.

'리소스 그룹'을 클릭한다.

좌측 상단에 '+만들기'를 누른다.

들어가자마자 기본/배포/네트워킹/모니터링/태그/검토+만들기 로 카테고리가 나눠진 화면이 보일 것이다. 각각에 대한 설명을 상세하게 적겠다.

기본 카테고리에서 할 일)

- 웹 앱을 누른다
- 구독 옆에는 Heckers Ground 설정한 후, 구독에 연결된 리소스 그룹에 rg-hg-byte를 입력한다.
- 게시는 코드를 선택한다.
- 런타임 스택에 Python 3.8을 선택한다.
- 운영체제 Linux를 선택한다.
- 지역에는 Korea Central을 선택한다.
  
배포에서 할 일)

-Github Action 설정 – 지속적인 배포 사용을 선택한다.
-Github 계정 권한부여를 누르고 뜨는 화면에 password를 입력한다.
-조직은 hackersground-kr
- 리포지토리는 Byte
- 분기는 main

*네트워킹, 모니터링, 태그는 패스한다.

검토+만들기)

-만들기를 누른다.

-배포 진행 중에서 배포가 완료됨이 뜰 때 까지 기다린다.

-배포가 완료됨이 뜨면 리소스로 이동을 누른다.

-이동을 누르면 나타나는 화면에 오른쪽 5번째 줄에 github프로젝트 옆에 있는 링크를 누른다.

그다음 Actions에 들어간다.

-build가 안 됐으면 안된 걸 확인해주고 오류를 고쳐준다. 오류가 고쳐지면 deploy 밑에 링크가 뜬다. 그 링크를 들어가서 welcome to azure 뜨면 배포가 성공된 것이다. 



