import React from 'react';
import { useTranslation } from 'react-i18next';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';
import ParticleBackground from '../components/ParticleBackground';

function HomepageHeader() {
  const { t } = useTranslation();

  return (
    <header className={styles.heroBanner}>
      <ParticleBackground />
      <div className={styles.heroContainer}>
        <div className={styles.heroContent}>
          <h1 className={styles.heroTitle}>
            {t('hero.title')}<span className={styles.highlight}>{t('hero.highlight')}</span>{t('hero.titleEnd')}
          </h1>
          <p className={styles.heroSubtitle}>
            {t('hero.subtitle')}
            <strong> {t('hero.free')}</strong>
          </p>
          <div className={styles.buttons}>
            <Link
              className={styles.primaryButton}
              to="/docs/intro">
              {t('hero.cta.browse')}
            </Link>
            <Link
              className={styles.secondaryButton}
              to="/chat">
              {t('hero.cta.personalize')}
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

function ModuleCard({ number, title, description, features }: any) {
  return (
    <div className={styles.moduleCard}>
      <div className={styles.moduleNumber}>Module {number}</div>
      <h3 className={styles.moduleTitle}>{title}</h3>
      <p className={styles.moduleDescription}>{description}</p>
      <ul className={styles.moduleFeatures}>
        {features.map((feature: string, idx: number) => (
          <li key={idx}>▸ {feature}</li>
        ))}
      </ul>
    </div>
  );
}

function ValueCard({ icon, title, description }: any) {
  return (
    <div className={styles.valueCard}>
      <div className={styles.valueIcon}>{icon}</div>
      <h3 className={styles.valueTitle}>{title}</h3>
      <p className={styles.valueDescription}>{description}</p>
    </div>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  const { t } = useTranslation();

  const modules = [
    {
      number: 1,
      title: "ROS 2 Fundamentals",
      description: "Master the robotic nervous system with ROS 2 middleware for robot control.",
      features: ["Nodes, Topics, and Services", "Python Agents with rclpy", "URDF for Humanoids"]
    },
    {
      number: 2,
      title: "Digital Twins",
      description: "Build physics simulations and high-fidelity environments.",
      features: ["Gazebo Physics Simulation", "Unity Visualization", "Sensor Simulation (LiDAR, IMU)"]
    },
    {
      number: 3,
      title: "NVIDIA Isaac",
      description: "Advanced perception, navigation, and sim-to-real transfer.",
      features: ["Isaac Sim & Synthetic Data", "VSLAM & Navigation", "Reinforcement Learning"]
    },
    {
      number: 4,
      title: "Vision-Language-Action",
      description: "Convergence of LLMs and Robotics for conversational control.",
      features: ["Voice-to-Action (Whisper)", "LLM Cognitive Planning", "Autonomous Humanoid Capstone"]
    }
  ];

  const values = [
    {
      icon: "🤖",
      title: "Embodied Intelligence",
      description: "AI that operates in physical space, not just digital environments. Robots that understand physics and interact with the real world."
    },
    {
      icon: "👤",
      title: "Human-Centered Design",
      description: "Humanoid robots navigate our world without modification. They use human tools, interfaces, and learn from demonstrations."
    },
    {
      icon: "⚡",
      title: "Production-Ready Skills",
      description: "ROS 2, Gazebo, NVIDIA Isaac, and VLA models. The complete stack for modern robotics development."
    },
    {
      icon: "💬",
      title: "Conversational Robotics",
      description: "Natural language commands translated to robot actions. 'Clean the room' becomes a sequence of coordinated movements."
    },
    {
      icon: "🔄",
      title: "Sim-to-Real Transfer",
      description: "Train in simulation, deploy to reality. Photorealistic environments and domain randomization bridge the gap."
    },
    {
      icon: "🎓",
      title: "Interactive Learning",
      description: "RAG-powered chat, personalized content, and hands-on exercises. Learn by doing, not just reading."
    }
  ];

  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics - Master ROS 2, Gazebo, NVIDIA Isaac, and Vision-Language-Action systems">
      <HomepageHeader />

      <main>
        {/* Journey Section */}
        <section className={styles.journeySection}>
          <div className="container">
            <h2 className={styles.sectionTitle}>{t('sections.journey.title')}</h2>
            <p className={styles.sectionSubtitle}>{t('sections.journey.subtitle')}</p>

            <div className={`${styles.modulesGrid} animate-stagger`}>
              {modules.map((module, idx) => (
                <ModuleCard key={idx} {...module} />
              ))}
            </div>
          </div>
        </section>

        {/* Value Propositions */}
        <section className={styles.valuesSection}>
          <div className="container">
            <h2 className={styles.sectionTitle}>{t('sections.values.title')}</h2>
            <p className={styles.sectionSubtitle}>{t('sections.values.subtitle')}</p>

            <div className={`${styles.valuesGrid} animate-stagger`}>
              {values.map((value, idx) => (
                <ValueCard key={idx} {...value} />
              ))}
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className={styles.ctaSection}>
          <div className="container">
            <h2 className={styles.ctaTitle}>{t('sections.cta.title')}</h2>
            <p className={styles.ctaSubtitle}>{t('sections.cta.subtitle')}</p>
            <p className={styles.ctaDescription}>
              {t('sections.cta.description')}
            </p>
            <div className={styles.ctaButtons}>
              <Link className={styles.primaryButton} to="/docs/intro">
                Start Your Journey
              </Link>
              <Link className={styles.secondaryButton} to="/chat">
                Personalize Your Path
              </Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
