@echo off
REM Batch script to generate all MDX templates at once
REM Run this from the textbook directory

echo Generating MDX templates for all remaining pages...
echo.

echo Module 1 pages...
python generate_mdx_template.py docs/module1/ros2-fundamentals.md docs/module1/ros2-fundamentals.mdx ROS2Fundamentals
python generate_mdx_template.py docs/module1/nodes-topics-services.md docs/module1/nodes-topics-services.mdx NodesTopicsServices
python generate_mdx_template.py docs/module1/python-integration.md docs/module1/python-integration.mdx PythonIntegration
python generate_mdx_template.py docs/module1/urdf.md docs/module1/urdf.mdx URDF

echo.
echo Module 2 pages...
python generate_mdx_template.py docs/module2/gazebo-simulation.md docs/module2/gazebo-simulation.mdx GazeboSimulation
python generate_mdx_template.py docs/module2/unity-integration.md docs/module2/unity-integration.mdx UnityIntegration
python generate_mdx_template.py docs/module2/sensor-simulation.md docs/module2/sensor-simulation.mdx SensorSimulation

echo.
echo Module 3 pages...
python generate_mdx_template.py docs/module3/isaac-sim.md docs/module3/isaac-sim.mdx IsaacSim
python generate_mdx_template.py docs/module3/isaac-ros.md docs/module3/isaac-ros.mdx IsaacROS
python generate_mdx_template.py docs/module3/nav2.md docs/module3/nav2.mdx Nav2

echo.
echo Module 4 pages...
python generate_mdx_template.py docs/module4/voice-to-action.md docs/module4/voice-to-action.mdx VoiceToAction
python generate_mdx_template.py docs/module4/llm-planning.md docs/module4/llm-planning.mdx LLMPlanning
python generate_mdx_template.py docs/module4/capstone-project.md docs/module4/capstone-project.mdx CapstoneProject

echo.
echo Resources pages...
python generate_mdx_template.py docs/resources/hardware-requirements.md docs/resources/hardware-requirements.mdx HardwareRequirements
python generate_mdx_template.py docs/resources/cloud-vs-local.md docs/resources/cloud-vs-local.mdx CloudVsLocal
python generate_mdx_template.py docs/resources/weekly-breakdown.md docs/resources/weekly-breakdown.mdx WeeklyBreakdown

echo.
echo ========================================
echo All templates generated!
echo.
echo Next steps:
echo 1. Open each .mdx file
echo 2. Translate the Urdu section using ChatGPT/Claude
echo 3. Save and test
echo.
echo See TRANSLATION_GUIDE.md for detailed instructions
echo ========================================
pause
