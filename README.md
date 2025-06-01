# FastAPI 项目空白模板 / FastAPI Project Blank Template

一个为中小型项目设计的 FastAPI 空白模板，提供了清晰的项目结构。

A blank template for FastAPI projects designed for small to medium-sized applications, providing a clear project structure.

## 项目结构 / Project Structure

```
fastapi_blank_template/
├── app/                    # 应用主目录
│   ├── api/                # API路由层 (可选 / Optional)
│   │   └── v1/             # API版本1
│   │       ├── __init__.py # 路由注册
│   │       └── hello.py    # 示例路由
│   ├── core/               # 核心配置 (可选 / Optional)
│   │   ├── __init__.py
│   │   └── config.py       # 应用配置
│   ├── crud/               # 数据库CRUD操作 (可选 / Optional)
│   ├── db/                 # 数据库连接和会话 (可选 / Optional)
│   ├── deps/               # 依赖项（认证、权限等）(可选 / Optional)
│   ├── exceptions/         # 自定义异常和异常处理 (可选 / Optional)
│   ├── middlewares/        # 自定义中间件 (可选 / Optional)
│   ├── models/             # ORM模型（SQLAlchemy等）(可选 / Optional)
│   ├── schemas/            # Pydantic模型 (可选 / Optional)
│   ├── services/           # 业务逻辑层 (可选 / Optional)
│   ├── tasks/              # 异步任务 (可选 / Optional)
│   ├── utils/              # 通用工具函数 (可选 / Optional)
│   ├── __init__.py
│   └── main.py             # 应用入口
├── docs/                   # 项目文档 (可选 / Optional)
├── migrations/             # 数据库迁移文件 (可选 / Optional)
├── static/                 # 静态文件 (可选 / Optional)
├── tests/                  # 测试用例 (可选 / Optional)
├── .env.example            # 环境变量示例 (可选 / Optional)
├── .env                    # 环境变量 (可选 / Optional, 被 .gitignore 忽略)
├── .gitignore              # Git忽略文件
├── .gitattributes          # Git配置文件
├── Dockerfile              # Docker配置 (可选 / Optional)
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
├── .gitignore              # Git忽略文件（推荐 / Recommended）
├── README.md               # 项目说明（推荐 / Recommended）
└── requirements.txt        # 依赖项
```

> **注意/Note:** 在最小结构中，所有路由都直接定义在 main.py 文件中，无需使用单独的 api 目录。需要注释或删除 main.py 中引入外部路由的代码（如 `from app.api.v1 import router as api_router` 和 `app.include_router(api_router, prefix="/api/v1")`），改为直接在 main.py 中定义路由。随着项目增长，再考虑将路由分离到 api 目录下。
>
> In the minimal structure, all routes are defined directly in the main.py file, without using a separate api directory. You need to comment out or remove the code in main.py that imports external routers (such as `from app.api.v1 import router as api_router` and `app.include_router(api_router, prefix="/api/v1")`). As the project grows, consider moving routes to the api directory.

## 目录说明 / Directory Explanation

### app/

应用主目录，包含所有源代码。

Main application directory containing all source code.

#### api/

API路由层，处理HTTP请求和响应。按版本组织（如v1, v2）便于API版本控制。

API routing layer that handles HTTP requests and responses. Organized by versions (e.g., v1, v2) for better API versioning.

#### core/

核心配置和设置，如应用配置、环境变量、日志配置等。

Core configurations and settings like app config, environment variables, logging setup, etc.

#### crud/

数据库CRUD（创建、读取、更新、删除）操作的封装。

Encapsulation of database CRUD (Create, Read, Update, Delete) operations.

#### db/

数据库连接、会话管理和通用数据库工具。

Database connections, session management, and general database utilities.

#### deps/

依赖项，如认证依赖、权限检查、分页参数等。用于FastAPI的依赖注入系统。

Dependencies like authentication, permission checks, pagination parameters, etc. Used for FastAPI's dependency injection system.

#### exceptions/

自定义异常类和异常处理器。

Custom exception classes and exception handlers.

#### middlewares/

自定义中间件，如请求ID生成、日志记录、性能监控等。

Custom middlewares like request ID generation, logging, performance monitoring, etc.

#### models/

ORM模型，如SQLAlchemy模型。定义数据库结构和关系。

ORM models like SQLAlchemy models. Defines database structure and relationships.

#### schemas/

Pydantic模型，用于请求验证、响应序列化和文档生成。

Pydantic models for request validation, response serialization, and documentation generation.

#### services/

业务逻辑层，实现核心业务功能，位于API路由和数据访问层之间。

Business logic layer that implements core business functionalities, sitting between API routes and data access.

#### tasks/

异步任务定义，如后台作业、定时任务等。

Asynchronous task definitions like background jobs, scheduled tasks, etc.

#### utils/

通用工具函数和助手模块。

General utility functions and helper modules.

### docs/

项目文档，如API文档、架构图、开发指南等。

Project documentation like API docs, architecture diagrams, development guides, etc.

### migrations/

数据库迁移文件，用于版本化数据库结构变更。

Database migration files for versioning database structure changes.

### static/

静态文件，如图片、CSS、JavaScript等。

Static files like images, CSS, JavaScript, etc.

### tests/

测试用例，包含单元测试、集成测试等。

Test cases including unit tests, integration tests, etc.

### 启动应用 / Start the Application

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

访问 / Access: http://localhost:8000/docs 查看API文档 / to see API documentation
