import time
import sys

class DigitalDetoxApp:
    def __init__(self, target_minutes=1):
        self.target_time_seconds = target_minutes * 60
        self.reward_points = 0
        self.is_blocking_active = False

    def activate_detox_mode(self):
        """Simulates system level interceptors to block incoming notifications."""
        self.is_blocking_active = True
        print("\n[SYSTEM] Intercepting notification channels...")
        print("[SYSTEM] SMS, WhatsApp, and social media notifications are now BLOCKED.")
        print(f"Starting your {self.target_time_seconds // 60}-minute focus session. Stay disciplined!\n")

    def run_focus_session(self):
        """Simulates the background countdown timer running on the mobile OS."""
        if not self.is_blocking_active:
            print("Please activate Detox Mode first.")
            return

        elapsed_time = 0
        try:
            while elapsed_time < self.target_time_seconds:
                # Calculate remaining time
                remaining = self.target_time_seconds - elapsed_time
                mins, secs = divmod(remaining, 60)
                time_str = f"{mins:02d}:{secs:02d}"
                
                # Print live countdown to the terminal screen dynamically
                sys.stdout.write(f"\rFocus Time Remaining: {time_str} | [STATUS: Notifications Suppressed]")
                sys.stdout.flush()
                
                time.sleep(1) # Simulate real-world passing seconds
                elapsed_time += 1
                
            self.complete_session()
            
        except KeyboardInterrupt:
            # Triggers if the user forces their way out of the session prematurely
            print("\n\n[WARNING] Session broken early! No rewards issued. Notification block lifted.")
            self.is_blocking_active = False

    def complete_session(self):
        """Calculates and updates user account states upon successful session completion."""
        self.is_blocking_active = False
        print("\n\n" + "="*50)
        print("🎉 SUCCESS! You completed your Digital Detox session!")
        print("="*50)
        
        # Gamification core logic: Allocate points based on minutes completed
        earned = (self.target_time_seconds // 60) * 10
        self.reward_points += earned
        
        print(f"[REWARD] You have successfully earned +{earned} Focus Points!")
        print(f"[WALLET] Current Total Balance: {self.reward_points} Points")
        print("[SYSTEM] Notification channels safely restored. Well done!")

# Core execution block to launch the simulated engine
if __name__ == "__main__":
    # Initialize a 1-minute simulated focus test block
    detox_engine = DigitalDetoxApp(target_minutes=1)
    detox_engine.activate_detox_mode()
    detox_engine.run_focus_session()
