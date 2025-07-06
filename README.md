# FastAPI 后端项目空白模板 | Backend Project Blank Template

<div align="center">

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

一个规范、清晰的 FastAPI 项目**空白模板**，仅提供目录结构参考

*A well-organized, clean FastAPI project **blank template** that provides directory structure reference only*

</div>

## 📚 简介 | Introduction

这是一个由我设计的纯粹**目录结构参考模板**，不包含实际功能代码（会随着经历和个人审美而更新）：

- **仅提供结构** - 文件夹和文件名仅作参考，不含实际业务逻辑
- **分层架构** - 建议的数据访问、业务逻辑和API层分离结构
- **实用参考** - 基于常见的FastAPI项目组织方式
- **灵活定制** - 可根据实际需求裁剪或扩展目录结构
- **结构清晰** - 为各模块的职责划分提供参考建议

*This is a pure **directory structure reference template** designed by me, without actual functional code.:*

- ***Structure Only** - Folders and file names are for reference only, containing no actual business logic*
- ***Layered Architecture** - Suggested structure for separating data access, business logic, and API layers*
- ***Practical Reference** - Based on common FastAPI project organization patterns*
- ***Flexible Customization** - Structure can be trimmed or expanded based on actual requirements*
- ***Clear Organization** - Provides reference suggestions for module responsibilities*

## 🗂️ 项目结构 | Project Structure

```
fastapi_blank_template/
├── app/                    # 应用主目录
│   ├── api/                # API路由层
│   │   └── v1/             # API版本v1
│   │       ├── __init__.py # 子路由聚合
│   │       ├── auth.py     # 认证相关路由
│   │       └── users.py    # 用户相关路由
│   ├── config/             # 配置相关
│   ├── constants/          # 常量定义
│   │   └── auth_constants.py # 认证相关常量
│   ├── db_core/            # 数据库连接和会话
│   ├── dependencies/       # 依赖项（认证、权限等）
│   │   └── auth/           # 认证相关依赖
│   │       └── jwt_provider.py # JWT提供器
│   ├── models/             # ORM模型（SQLAlchemy等）
│   │   └── user.py         # 用户模型
│   ├── exceptions/         # 自定义异常和异常处理
│   │   ├── auth_errors.py  # 认证相关错误
│   │   └── handlers.py     # 全局异常处理器
│   ├── middlewares/        # 自定义中间件
│   │   └── logging_middleware.py # 日志中间件
│   ├── dal/                # 数据访问层
│   │   ├── base_repository.py # 基础仓库
│   │   └── user_repository.py # 用户仓库
│   ├── schemas/            # Pydantic模型
│   │   ├── __init__.py
│   │   └── users_schemas.py # 用户相关模式
│   ├── services/           # 业务逻辑层
│   │   └── user_service.py # 用户服务
│   ├── task_queues/        # 异步任务
│   │   └── email_queue.py  # 邮件队列
│   ├── utils/              # 通用工具函数
│   │   └── security_utils.py # 安全相关工具
│   ├── __init__.py
│   └── main.py             # 应用入口
├── docs/                   # 项目文档
├── migrations/             # 数据库迁移文件
├── tests/                  # 测试用例
├── .env.example            # 环境变量示例
├── .gitignore              # Git忽略文件
├── .gitattributes          # Git配置文件
├── Dockerfile              # Docker配置，我一般在上一级写docker-compose.yaml
├── README.md               # 项目说明
└── requirements.txt        # 依赖项
```

> **注意/Note:** 上述文件结构中列出的文件名仅提供命名参考，不包含实际代码。您可以根据项目需求自行实现这些文件的内容。
>
> The file names listed in the structure above are for reference only and do not contain actual code. You can implement the content of these files according to your project requirements.

## 目录说明 | Directory Explanation

### app/

应用主目录，包含所有源代码。

Main application directory containing all source code.

#### api/

API路由层，处理HTTP请求和响应。按版本组织（如v1, v2）便于API版本控制。

API routing layer that handles HTTP requests and responses. Organized by versions (e.g., v1, v2) for better API versioning.

#### constants/

常量定义模块，用于存储应用中的常量值。

Constants definition module for storing constant values used in the application.

#### db_core/

数据库连接、会话管理和通用数据库工具。

Database connections, session management, and general database utilities.

#### dependencies/

依赖项，如认证依赖、权限检查、分页参数等。用于FastAPI的依赖注入系统。

Dependencies like authentication, permission checks, pagination parameters, etc. Used for FastAPI's dependency injection system.

##### auth/

认证相关依赖。

Authentication-related dependencies.

#### models/

ORM模型，如SQLAlchemy, Tortoise模型。定义数据库结构和关系。

ORM models like SQLAlchemy , Tortoise models. Defines database structure and relationships.

#### exceptions/

自定义异常类和异常处理器。

Custom exception classes and exception handlers.

#### middlewares/

自定义中间件，如请求ID生成、日志记录、性能监控等。

Custom middlewares like request ID generation, logging, performance monitoring, etc.

#### dal/

数据访问层，封装复杂的数据库查询逻辑。

Data access layer that encapsulates complex database query logic.

#### schemas/

Pydantic模型，用于请求验证、响应序列化和文档生成。

Pydantic models for request validation, response serialization, and documentation generation.

#### services/

业务逻辑层，实现核心业务功能，位于API路由和数据访问层之间。

Business logic layer that implements core business functionalities, sitting between API routes and data access.

#### config/

配置相关模块，如应用设置、环境变量等。

Settings-related modules like app settings, environment variables, etc.

#### task_queues/

异步任务定义，如后台作业、定时任务等。

Asynchronous task definitions like background jobs, scheduled tasks, etc.

#### utils/

通用工具函数和助手模块。

General utility functions and helper modules.

### docs/

项目文档，包含设计文档、API文档等。

Project documentation including design documents, API documentation, etc.

### migrations/

数据库迁移文件，用于版本化数据库结构变更。

Database migration files for versioning database structure changes.

### tests/

测试用例，包含单元测试、集成测试等。

Test cases including unit tests, integration tests, etc.

> **提示/Tip:** 如果你是FastAPI新手，请参考官方文档学习：https://fastapi.tiangolo.com/
>
> If you are new to FastAPI, please refer to the official documentation: https://fastapi.tiangolo.com/

## 启动应用 | Start the Application

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

访问 / Access: http://localhost:8000/docs 查看API文档 / to see API documentation
