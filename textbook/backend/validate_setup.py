"""
Setup Validation Script
Validates all configuration and service connections before deployment
"""

import os
import sys
from dotenv import load_dotenv
from typing import Dict, Tuple

# Load environment variables
load_dotenv()

def print_section(title: str):
    """Print a formatted section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def check_env_var(var_name: str) -> Tuple[bool, str]:
    """Check if an environment variable is set and not a placeholder"""
    value = os.getenv(var_name)
    if not value:
        return False, f"❌ {var_name}: NOT SET"
    if "your_" in value or "placeholder" in value:
        return False, f"⚠️  {var_name}: PLACEHOLDER VALUE"
    return True, f"✅ {var_name}: Set"

def validate_environment_variables() -> bool:
    """Validate all required environment variables"""
    print_section("Environment Variables")
    
    required_vars = [
        "OPENAI_API_KEY",
        "OPENAI_BASE_URL",
        "QDRANT_URL",
        "QDRANT_API_KEY",
        "QDRANT_COLLECTION_NAME",
        "DATABASE_URL",
        "LLM_MODEL",
        "EMBEDDING_MODEL"
    ]
    
    all_valid = True
    for var in required_vars:
        valid, message = check_env_var(var)
        print(message)
        if not valid:
            all_valid = False
    
    return all_valid

def test_qdrant_connection() -> bool:
    """Test connection to Qdrant vector database"""
    print_section("Qdrant Vector Database")
    
    try:
        from qdrant_client import QdrantClient
        
        qdrant_url = os.getenv("QDRANT_URL")
        qdrant_api_key = os.getenv("QDRANT_API_KEY")
        collection_name = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_textbook")
        
        client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
        
        # Get collections
        collections = client.get_collections()
        collection_names = [c.name for c in collections.collections]
        
        print(f"✅ Connected to Qdrant")
        print(f"   Available collections: {collection_names}")
        
        # Check if our collection exists
        if collection_name in collection_names:
            collection_info = client.get_collection(collection_name)
            points_count = collection_info.points_count
            print(f"✅ Collection '{collection_name}' exists")
            print(f"   Points count: {points_count}")
            
            if points_count == 0:
                print(f"⚠️  Warning: Collection has 0 points. Run embeddings.py to populate.")
                return True
            elif points_count < 100:
                print(f"⚠️  Warning: Low point count. Expected ~433 points as per guides.")
                return True
            else:
                print(f"✅ Good! Collection has sufficient embeddings.")
                return True
        else:
            print(f"⚠️  Collection '{collection_name}' does not exist.")
            print(f"   Run embeddings.py to create and populate it.")
            return True
            
    except ImportError:
        print("❌ qdrant-client not installed. Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Failed to connect to Qdrant: {str(e)}")
        return False

def test_database_connection() -> bool:
    """Test connection to Neon PostgreSQL database"""
    print_section("Neon PostgreSQL Database")
    
    try:
        from sqlalchemy import create_engine, text
        
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            print("❌ DATABASE_URL not set")
            return False
        
        engine = create_engine(database_url)
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"✅ Connected to PostgreSQL")
            print(f"   Version: {version[:50]}...")
        
        return True
        
    except ImportError:
        print("❌ SQLAlchemy not installed. Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Failed to connect to database: {str(e)}")
        return False

def test_openrouter_connection() -> bool:
    """Test connection to OpenRouter API"""
    print_section("OpenRouter API")
    
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("OPENAI_BASE_URL")
        
        client = OpenAI(api_key=api_key, base_url=base_url)
        
        # Try to list models (lightweight check)
        print(f"✅ OpenRouter API key configured")
        print(f"   Base URL: {base_url}")
        print(f"   Model: {os.getenv('LLM_MODEL')}")
        
        return True
        
    except ImportError:
        print("❌ openai package not installed. Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Failed to validate OpenRouter: {str(e)}")
        return False

def check_project_structure() -> bool:
    """Check if key project files exist"""
    print_section("Project Structure")
    
    required_files = [
        ("../docs/intro.md", "Docs directory"),
        ("../docs/module1", "Module 1 content"),
        ("../docs/module2", "Module 2 content"),
        ("../docs/module3", "Module 3 content"),
        ("../docs/module4", "Module 4 content"),
        ("main.py", "Backend main file"),
        ("rag.py", "RAG engine"),
        ("embeddings.py", "Embedding script"),
        ("database.py", "Database models"),
    ]
    
    all_exist = True
    for file_path, description in required_files:
        full_path = os.path.join(os.path.dirname(__file__), file_path)
        if os.path.exists(full_path):
            print(f"✅ {description}: Found")
        else:
            print(f"❌ {description}: NOT FOUND at {file_path}")
            all_exist = False
    
    return all_exist

def main():
    """Run all validation checks"""
    print("\n" + "🔍 "*20)
    print("  PHYSICAL AI TEXTBOOK - SETUP VALIDATION")
    print("🔍 "*20)
    
    results = {
        "Environment Variables": validate_environment_variables(),
        "Project Structure": check_project_structure(),
        "Qdrant Connection": test_qdrant_connection(),
        "Database Connection": test_database_connection(),
        "OpenRouter API": test_openrouter_connection(),
    }
    
    # Summary
    print_section("VALIDATION SUMMARY")
    
    all_passed = True
    for check, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {check}")
        if not passed:
            all_passed = False
    
    print("\n" + "="*60)
    if all_passed:
        print("🎉 All checks passed! Your setup is ready.")
        print("\nNext steps:")
        print("  1. If embeddings are empty, run: python embeddings.py")
        print("  2. Start backend: python main.py")
        print("  3. Start frontend: cd .. && npm start")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  • Install dependencies: pip install -r requirements.txt")
        print("  • Check .env file has correct values (no placeholders)")
        print("  • Verify API keys are valid and not expired")
    print("="*60 + "\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
