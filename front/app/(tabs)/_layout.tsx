import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { HapticTab } from "../../components/HapticTab";
import ChatScreen from "../../screens/ChatScreen";

const Tab = createBottomTabNavigator();

export default function MyTabs() {
  return (
    <Tab.Navigator
      screenOptions={{
        tabBarButton: (props) => <HapticTab {...props} />,
      }}
    >
      <Tab.Screen
        name="ChatScreen"
        component={ChatScreen}
      />
      {/* Add more tabs as needed */}
    </Tab.Navigator>
  );
}