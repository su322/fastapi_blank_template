# FastAPI 后端项目空白模板 / FastAPI Backend Project Blank Template

一个为中小型项目设计的 FastAPI 后端空白模板，提供了清晰的项目结构。本模板采用分层架构设计，严格遵循关注点分离原则，将数据访问、业务逻辑和表示层清晰分开。架构设计遵循依赖倒置原则，通过依赖注入实现模块间的低耦合，便于单元测试和功能扩展。同时支持异步操作和中间件集成，适合构建高性能、可扩展的 RESTful API 服务。

A blank backend template for FastAPI projects designed for small to medium-sized applications, providing a clear project structure. This template follows a layered architecture design, strictly adhering to the separation of concerns principle by clearly separating data access, business logic, and presentation layers. The architecture follows the dependency inversion principle, implementing low coupling between modules through dependency injection, facilitating unit testing and feature extensions. It also supports asynchronous operations and middleware integration, making it suitable for building high-performance, scalable RESTful API services.

## 项目结构 / Project Structure

```
fastapi_blank_template/
├── app/                    # 应用主目录
│   ├── api/                # API路由层
│   │   └── v1/             # API版本1
│   │       ├── __init__.py # 路由注册
│   │       └── hello.py    # 示例路由
│   ├── config/             # 配置相关
│   ├── db_core/            # 数据库连接和会话
│   ├── dependencies/       # 依赖项（认证、权限等）
│   │   └── auth/           # 认证相关依赖
│   ├── entities/           # ORM模型（SQLAlchemy等）
│   ├── exceptions/         # 自定义异常和异常处理
│   ├── middlewares/        # 自定义中间件
│   ├── repositories/       # 数据库仓库层
│   ├── schemas/            # Pydantic模型
│   ├── services/           # 业务逻辑层
│   ├── tasks/              # 异步任务
│   ├── utils/              # 通用工具函数
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

## 最小目录结构 / Minimal Structure

对于快速启动和简单示例，只需要以下结构：

For quick start and simple examples, only the following structure is required:

```
fastapi_blank_template/
├── app/
│   ├── __init__.py
│   └── main.py             # 应用入口
└── requirements.txt        # 依赖项
```

> **注意/Note:** 在最小结构中，所有路由都直接定义在 main.py 文件中，无需使用单独的 api 目录。需要注释或删除 main.py 中引入外部路由的代码（如 `from app.api.v1 import router as api_router` 和 `app.include_router(api_router, prefix="/api/v1")`），改为直接在 main.py 中定义路由。
>
> In the minimal structure, all routes are defined directly in the main.py file, without using a separate api directory. You need to comment out or remove the code in main.py that imports external routers (such as `from app.api.v1 import router as api_router` and `app.include_router(api_router, prefix="/api/v1")`).

## 目录说明 / Directory Explanation

### app/

应用主目录，包含所有源代码。

Main application directory containing all source code.

#### api/

API路由层，处理HTTP请求和响应。按版本组织（如v1, v2）便于API版本控制。

API routing layer that handles HTTP requests and responses. Organized by versions (e.g., v1, v2) for better API versioning.

#### crud/

数据库CRUD（创建、读取、更新、删除）操作的封装。

Encapsulation of database CRUD (Create, Read, Update, Delete) operations.

#### db_core/

数据库连接、会话管理和通用数据库工具。

Database connections, session management, and general database utilities.

#### dependencies/

依赖项，如认证依赖、权限检查、分页参数等。用于FastAPI的依赖注入系统。

Dependencies like authentication, permission checks, pagination parameters, etc. Used for FastAPI's dependency injection system.

##### auth/

认证相关依赖。

Authentication-related dependencies.

#### entities/

ORM模型，如SQLAlchemy, Tortoise模型。定义数据库结构和关系。

ORM models like SQLAlchemy , Tortoise models. Defines database structure and relationships.

#### exceptions/

自定义异常类和异常处理器。

Custom exception classes and exception handlers.

#### middlewares/

自定义中间件，如请求ID生成、日志记录、性能监控等。

Custom middlewares like request ID generation, logging, performance monitoring, etc.

#### repositories/

数据库仓库层，封装复杂的数据库查询逻辑。

Database repository layer that encapsulates complex database query logic.

#### schemas/

Pydantic模型，用于请求验证、响应序列化和文档生成。

Pydantic models for request validation, response serialization, and documentation generation.

#### services/

业务逻辑层，实现核心业务功能，位于API路由和数据访问层之间。

Business logic layer that implements core business functionalities, sitting between API routes and data access.

#### config/

配置相关模块，如应用设置、环境变量等。

Settings-related modules like app settings, environment variables, etc.

#### tasks/

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

## 启动应用 / Start the Application

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

访问 / Access: http://localhost:8000/docs 查看API文档 / to see API documentation
