# Quick Translation Guide

## 📋 What You Need to Do

You have **16 pages** left to translate. I've created all the infrastructure - you just need to add Urdu content!

## 🚀 Quick Process (5-10 min per page)

### Step 1: Generate Template
```bash
cd d:\physical-ai-textbook\textbook

# Example for Module 1 ROS2 Fundamentals
python generate_mdx_template.py docs/module1/ros2-fundamentals.md docs/module1/ros2-fundamentals.mdx ROS2Fundamentals
```

### Step 2: Get Urdu Translation
1. Open the generated `.mdx` file
2. Copy the English content from the `return (<div>...</div>)` section
3. Use ChatGPT/Claude with this prompt:

```
Translate the following Physical AI & Robotics documentation to Urdu.
Keep technical terms (ROS 2, Python, Gazebo, etc.) in English.
Translate explanations, descriptions, and instructions to Urdu.
Maintain all HTML tags exactly as they are.
Use proper Urdu terminology for robotics and AI concepts.

[PASTE ENGLISH HTML CONTENT HERE]
```

### Step 3: Insert Translation
1. Replace the `{/* TODO */}` section in the `if (isUrdu)` block
2. Paste the translated Urdu HTML from ChatGPT
3. Save the file

### Step 4: Clean Up
```bash
# Delete the old .md file
Remove-Item docs/module1/ros2-fundamentals.md
```

### Step 5: Test
1. Refresh your browser
2. Switch to Urdu language
3. Navigate to the page
4. Verify Gurjar font and RTL layout work

## 📝 Remaining Pages to Convert

### Module 1 (4 pages)
```bash
python generate_mdx_template.py docs/module1/ros2-fundamentals.md docs/module1/ros2-fundamentals.mdx ROS2Fundamentals
python generate_mdx_template.py docs/module1/nodes-topics-services.md docs/module1/nodes-topics-services.mdx NodesTopicsServices
python generate_mdx_template.py docs/module1/python-integration.md docs/module1/python-integration.mdx PythonIntegration
python generate_mdx_template.py docs/module1/urdf.md docs/module1/urdf.mdx URDF
```

### Module 2 (3 pages)
```bash
python generate_mdx_template.py docs/module2/gazebo-simulation.md docs/module2/gazebo-simulation.mdx GazeboSimulation
python generate_mdx_template.py docs/module2/unity-integration.md docs/module2/unity-integration.mdx UnityIntegration
python generate_mdx_template.py docs/module2/sensor-simulation.md docs/module2/sensor-simulation.mdx SensorSimulation
```

### Module 3 (3 pages)
```bash
python generate_mdx_template.py docs/module3/isaac-sim.md docs/module3/isaac-sim.mdx IsaacSim
python generate_mdx_template.py docs/module3/isaac-ros.md docs/module3/isaac-ros.mdx IsaacROS
python generate_mdx_template.py docs/module3/nav2.md docs/module3/nav2.mdx Nav2
```

### Module 4 (3 pages)
```bash
python generate_mdx_template.py docs/module4/voice-to-action.md docs/module4/voice-to-action.mdx VoiceToAction
python generate_mdx_template.py docs/module4/llm-planning.md docs/module4/llm-planning.mdx LLMPlanning
python generate_mdx_template.py docs/module4/capstone-project.md docs/module4/capstone-project.mdx CapstoneProject
```

### Resources (3 pages)
```bash
python generate_mdx_template.py docs/resources/hardware-requirements.md docs/resources/hardware-requirements.mdx HardwareRequirements
python generate_mdx_template.py docs/resources/cloud-vs-local.md docs/resources/cloud-vs-local.mdx CloudVsLocal
python generate_mdx_template.py docs/resources/weekly-breakdown.md docs/resources/weekly-breakdown.mdx WeeklyBreakdown
```

## ⚡ Pro Tips

1. **Batch translate**: Copy all English content for one module, translate together
2. **Keep code blocks in English**: Don't translate variable names, code examples
3. **Technical terms**: ROS 2, Python, Gazebo, Isaac, Unity → keep in English
4. **Review**: AI translation is 90% accurate, review for technical correctness
5. **Test as you go**: Check each page after translation

## 🎯 What's Already Done

✅ Sidebar - all labels in Urdu
✅ Homepage - fully bilingual  
✅ Intro page - fully bilingual
✅ All 4 module overviews - fully bilingual
✅ Gulzar font - automatically applies
✅ RTL layout - automatically works

## 📊 Estimated Time

- Generate template: 30 seconds
- Get translation: 3-5 minutes (ChatGPT)
- Insert + test: 2-3 minutes
- **Total per page: ~6-8 minutes**
- **All 16 pages: ~2 hours** (if done in one sitting)

## 🆘 If You Have Issues

1. **Syntax errors**: Make sure all HTML tags are closed
2. **Page won't load**: Check console for errors, verify component name matches function name
3. **Urdu not showing**: Clear cache, check language switcher
4. **Font issues**: Verify `src/css/urdu-font.css` is imported

## ✨ You're Almost Done!

Once all 16 pages are translated, you'll have a **completely bilingual Physical AI textbook** with beautiful Urdu typography!
