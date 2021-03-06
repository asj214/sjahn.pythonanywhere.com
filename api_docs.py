template = {
    "info": {
        "description": "powered by Flasgger",
        "termsOfService": "/tos",
        "title": "sjahn.pythonanywhere.com",
        "version": "0.0.1"
    },
    "basePath": "/",
    "paths": {
        "/api/user": {
            "get": {
                "security": [
                    {"bearerAuth": []}
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "회원 정보 조회",
                "tags": ["users"]
            },
            "post": {
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "email": {
                                        "default": '',
                                        "example": 'asj214@naver.com',
                                        "type": "string"
                                    },
                                    "name": {
                                        "default": '',
                                        "example": 'sjahn',
                                        "type": "string"
                                    },
                                    "password": {
                                        "default": '',
                                        "example": '1234',
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "회원 가입",
                "tags": ["users"]
            }
        },
        "/api/user/login": {
            "post": {
                
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "email": {
                                        "default": '',
                                        "example": 'asj214@naver.com',
                                        "type": "string"
                                    },
                                    "password": {
                                        "default": '',
                                        "example": '1234',
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "로그인",
                "tags": ["users"]
            }
        },

        "/api/banners": {
            "get": {
                "parameters": [
                    {
                        "name": "page",
                        "in": "query",
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    },
                    {
                        "name": "per_page",
                        "in": "query",
                        "schema": {
                            "type": "integer",
                            "default": 20,
                            "example": 20
                        }
                    },
                    {
                        "name": "category_id",
                        "in": "query",
                        "schema": {
                            "type": "integer",
                            "default": 1,
                            "example": 1
                        }
                    }
                ],
                "responses": {
                    "200": {"description": "OK"}
                },
                "summary": "배너 리스트",
                "tags": ["banners"]
            }
        }

    },
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    }

}