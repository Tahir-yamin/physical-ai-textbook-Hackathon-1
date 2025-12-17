import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction',
    },
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        { type: 'doc', id: 'module1/overview', label: 'Overview' },
        { type: 'doc', id: 'module1/ros2-fundamentals', label: 'ROS 2 Fundamentals' },
        { type: 'doc', id: 'module1/nodes-topics-services', label: 'Nodes, Topics & Services' },
        { type: 'doc', id: 'module1/python-integration', label: 'Python Integration' },
        { type: 'doc', id: 'module1/urdf', label: 'URDF for Humanoids' },
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      items: [
        { type: 'doc', id: 'module2/overview', label: 'Overview' },
        { type: 'doc', id: 'module2/gazebo-simulation', label: 'Gazebo Simulation' },
        { type: 'doc', id: 'module2/unity-integration', label: 'Unity Integration' },
        { type: 'doc', id: 'module2/sensor-simulation', label: 'Sensor Simulation' },
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      items: [
        { type: 'doc', id: 'module3/overview', label: 'Overview' },
        { type: 'doc', id: 'module3/isaac-sim-setup', label: 'Isaac Sim Setup' },
        { type: 'doc', id: 'module3/isaac-gym-rl', label: 'Isaac Gym RL' },
        { type: 'doc', id: 'module3/omniverse-replicator', label: 'Synthetic Data (Replicator)' },
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Voice-to-Action (VLA)',
      items: [
        { type: 'doc', id: 'module4/overview', label: 'Overview' },
        { type: 'doc', id: 'module4/whisper-integration', label: 'Speech Recognition (Whisper)' },
        { type: 'doc', id: 'module4/llm-action-parsing', label: 'Intent Parsing (LLM)' },
        { type: 'doc', id: 'module4/voice-command-pipeline', label: 'Voice Pipeline' },
      ],
    },
    {
      type: 'category',
      label: 'Resources',
      items: [
        { type: 'doc', id: 'resources/ros2-cheatsheet', label: 'ROS 2 Cheatsheet' },
        { type: 'doc', id: 'resources/python-api-reference', label: 'Python API Reference' },
        { type: 'doc', id: 'resources/troubleshooting', label: 'Troubleshooting' },
      ],
    },
  ],
};

export default sidebars;
